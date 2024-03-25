import datetime
from email.headerregistry import Group
from django.db import models
from django.core.exceptions import ValidationError
import re
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group

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
    
class Relatives(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    residential_address = models.CharField(max_length=200)
    e_mail = models.CharField(max_length=100, validators=[validate_email])

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
    leaving_date = models.DateField(blank=True, null=True)#, validators=[validate_leaving_date])
    photo_path = models.CharField(null=True, max_length = 100)
    relatives = models.ManyToManyField(Relatives)

    def clean(self):
        super().clean()
        validate_pesel(self.pesel, self.birth_date)
        if self.leaving_date:
            validate_leaving_date(self.admission_date, self.leaving_date)

class Notes(models.Model):
    child_id = models.ForeignKey(Children, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    contents = models.TextField()

class CustomUserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('A user email is needed.')

		if not password:
			raise ValueError('A user password is needed.')

		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password=None):
		if not email:
			raise ValueError('A user email is needed.')

		if not password:
			raise ValueError('A user password is needed.')

		user = self.create_user(email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    # Use django.contrib.auth.models.Group
    groups = models.ManyToManyField(Group, related_name='custom_user_set')

    # Add related_name arguments to resolve clashes
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

    def __str__(self):
        return self.email

# class Users(models.Model):
#     first_name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=100)
#     e_mail = models.CharField(max_length=100, validators=[validate_email])
#     password = models.CharField()

# class Documents(models.Model):
#     name = models.CharField(max_length = 50)
#     doc_type = models.CharField(max_length = 20)
#     date = models.DateField()
#     path = models.CharField(max_length=100)
#     child_pesel = models.ForeignKey(Children, on_delete=models.CASCADE)
    