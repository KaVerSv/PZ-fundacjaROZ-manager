# fixtures.py

from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_number(length):
    digits = string.digits
    return ''.join(random.choice(digits) for _ in range(length))

def add_example_data(**kwargs):
    from .models import Relatives, Children, Notes

    # Tworzymy 10 krewnych z różnymi danymi
    relatives = []
    for _ in range(10):
        relative = Relatives.objects.create(
            first_name=generate_random_string(random.randint(3, 10)),
            second_name=generate_random_string(random.randint(3, 10)),
            surname=generate_random_string(random.randint(3, 10)),
            phone_number=generate_random_number(9),
            residential_address=f'{random.randint(1, 100)} Main St, City',
            e_mail=f'{generate_random_string(5)}.{generate_random_string(5)}@example.com'
        )
        relatives.append(relative)

    # Tworzymy 10 dzieci z różnymi danymi
    children = []
    for i in range(10):
        child = Children.objects.create(
            pesel=generate_random_number(11),
            first_name=generate_random_string(random.randint(3, 10)),
            second_name=generate_random_string(random.randint(3, 10)),
            surname=generate_random_string(random.randint(3, 10)),
            gender=random.choice(['Female', 'Male']),
            birth_date=timezone.now().date() - timedelta(days=365*random.randint(1, 10)),
            birthplace=random.choice(["City Hospital", "Town Clinic", "Village Clinic"]),
            residential_address=f'{random.randint(1, 1000)} Elm St, Town',
            registered_address=f'{random.randint(1, 1000)} Oak St, Village',
            admission_date=timezone.now().date() - timedelta(days=365*random.randint(1, 5)),
            photo_path=f'{generate_random_string(10)}.jpg'
        )

        # Losowo przypisujemy 1 lub 2 krewnych do dziecka
        random_relatives = random.sample(relatives, random.randint(1, 2))
        for relative in random_relatives:
            child.relatives.add(relative)

        children.append(child)

    # Tworzymy notatki dla każdego dziecka
    for child in children:
        # Losowo generujemy liczbę notatek (0-3)
        num_notes = random.randint(0, 3)
        for _ in range(num_notes):
            Notes.objects.create(
                child_id=child,
                title=f'Note {_}',
                contents=f'Note content for child {child.id}'
            )
