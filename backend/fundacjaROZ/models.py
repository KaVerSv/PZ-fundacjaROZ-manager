import datetime
from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_email(value):
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not email_regex.match(value):
        raise ValidationError("Invalid email address!")
    
def validate_pesel(pesel, birth_date):
    if len(pesel) != 11:
        raise ValidationError("PESEL must be 11 digits long")

    if not pesel.isdigit():
        raise ValidationError("PESEL must contain only digits")

    if int(pesel[2]) < 2:
        pesel_birth_date = [1,9] + pesel[:6]
    else:
        pesel_birth_date = [2,0] + pesel[:2] + str(int(pesel[2]) - 2) + pesel[3:6]

    try:
        pesel_birth_date = datetime.datetime.strptime(pesel_birth_date, "%Y%m%d").date()
    except ValueError:
        raise ValidationError("Invalid PESEL birth date")

    if pesel_birth_date != birth_date:
        raise ValidationError("PESEL doesn't match to birth date")
    
def validate_leaving_date(admission_date, leaving_date):
    if admission_date > leaving_date or leaving_date > datetime.date.today():
        raise ValidationError("Wrong leaving date!!!")
    
def validate_admission_date(admission_date):
    if admission_date > datetime.date.today():
        raise ValidationError("Wrong admission date!!!")
    
class Children(models.Model):
    pesel = models.CharField(unique=True, max_length=11)#, validators=[validate_pesel]
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    birth_date = models.DateField()
    birthplace = models.CharField(max_length=100)
    residential_address = models.CharField(max_length=200)
    registered_address = models.CharField(max_length=200)
    admission_date = models.DateField(validators=[validate_admission_date])
    leaving_date = models.DateField(blank=True, null=True, validators=[validate_leaving_date])
    photo_path = models.CharField(max_length = 100)

    def clean(self):
        super().clean()
        validate_pesel(self.pesel, self.birth_date)
        if self.leaving_date:
            validate_leaving_date(self.admission_date, self.leaving_date)

class Notes(models.Model):
    child_id = models.ForeignKey(Children, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    contents = models.TextField()

class Relatives(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    residential_address = models.CharField(max_length=200)
    e_mail = models.CharField(max_length=100, validators=[validate_email])

class Association(models.Model):
    relative_id = models.ForeignKey(Relatives, on_delete=models.CASCADE)
    child_id = models.ForeignKey(Children, on_delete=models.CASCADE)
    association_type = models.CharField(max_length=20)

class Users(models.Model):
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    e_mail = models.CharField(max_length=100, validators=[validate_email])
    password = models.CharField()

# class Documents(models.Model):
#     name = models.CharField(max_length = 50)
#     doc_type = models.CharField(max_length = 20)
#     date = models.DateField()
#     path = models.CharField(max_length=100)
#     child_pesel = models.ForeignKey(Children, on_delete=models.CASCADE)
    