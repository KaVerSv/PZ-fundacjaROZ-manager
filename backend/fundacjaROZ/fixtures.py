# fixtures.py
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from .models import Relatives, Children, Notes

def add_example_data():
    # Tworzenie przykładowego krewnego
    relative = Relatives.objects.create(
        first_name='John',
        second_name='Doe',
        surname='Smith',
        phone_number='123456789',
        residential_address='123 Main St, City',
        e_mail='john.doe@example.com'
    )

    # Tworzenie przykładowego dziecka
    child1 = Children.objects.create(
        pesel='12345678901',
        first_name='Alice',
        second_name='Jane',
        surname='Doe',
        gender='Female',
        birth_date=timezone.now().date() - timedelta(days=365*5), # Example birthdate for a 5-year-old
        birthplace='City Hospital',
        residential_address='456 Elm St, Town',
        registered_address='789 Oak St, Village',
        admission_date=timezone.now().date() - timedelta(days=365), # Example admission date (1 year ago)
        photo_path='photos/alice_doe.jpg'
    )

    # Dodanie relatywnego krewnego do dziecka
    child1.relatives.add(relative)

    # Tworzenie drugiego przykładowego dziecka
    child2 = Children.objects.create(
        pesel='98765432109',
        first_name='Bob',
        second_name='Michael',
        surname='Smith',
        gender='Male',
        birth_date=timezone.now().date() - timedelta(days=365*7), # Example birthdate for a 7-year-old
        birthplace='Town Clinic',
        residential_address='123 Maple St, City',
        registered_address='456 Pine St, Suburb',
        admission_date=timezone.now().date() - timedelta(days=365*2), # Example admission date (2 years ago)
        leaving_date=timezone.now().date() - timedelta(days=365), # Example leaving date (1 year ago)
        photo_path='photos/bob_smith.jpg'
    )

    # Tworzenie notatek
    Notes.objects.create(
        child_id=child1,
        title='Health Note',
        contents='Allergic to peanuts.'
    )

    Notes.objects.create(
        child_id=child2,
        title='Behavior Note',
        contents='Requires extra attention in class.'
    )
