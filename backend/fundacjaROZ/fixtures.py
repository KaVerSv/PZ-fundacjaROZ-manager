# fixtures.py

from django.utils import timezone
from datetime import timedelta

def add_example_data(**kwargs):
    from .models import Relatives, Children, Notes, Users

    relatives_data = [
        {
            'first_name': 'John',
            'second_name': 'Doe',
            'surname': 'Smith',
            'phone_number': '123456789',
            'residential_address': '123 Main St, City',
            'e_mail': 'john.doe@example.com'
        },
        {
            'first_name': 'Jan',
            'second_name': 'Andrzej',
            'surname': 'Nowak',
            'phone_number': '987654321',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'jan.nowak@example.com'
        },
        {
            'first_name': 'Jan',
            'second_name': 'Paweł',
            'surname': 'Drugi',
            'phone_number': '987654333',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'jan.drugi@example.com'
        },
        {
            'first_name': 'Franek',
            'second_name': '',
            'surname': 'Dolas',
            'phone_number': '999654321',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'franek.dolas@example.com'
        },
        {
            'first_name': 'Piotr',
            'second_name': '',
            'surname': 'Więcek',
            'phone_number': '987333333',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'piotr.wiecek@example.com'
        },
        {
            'first_name': 'Marek',
            'second_name': '',
            'surname': 'Aureliusz',
            'phone_number': '333654321',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'marek.aureliusz@example.com'
        },
        {
            'first_name': 'Walenty',
            'second_name': '',
            'surname': 'Kwicoł',
            'phone_number': '987333321',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'walenty.kwicoł@example.com'
        },

        {
            'first_name': 'Jądruś',
            'second_name': 'Mati',
            'surname': 'Pyzdra',
            'phone_number': '333333321',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'jadrus.pyzdra@example.com'
        },
    ]

    children_data = [
        {
            'pesel': '12345678901',
            'first_name': 'Alice',
            'second_name': 'Jane',
            'surname': 'Doe',
            'gender': 'Female',
            'birth_date': timezone.now().date() - timedelta(days=365*13),
            'birthplace': 'City Hospital',
            'residential_address': '456 Elm St, Town',
            'registered_address': '789 Oak St, Village',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '1.jpg',
            'leaving_date': timezone.now().date() - timedelta(days=365),
        },
        {
            'pesel': '23456789013',
            'first_name': 'Emily',
            'second_name': 'Grace',
            'surname': 'Brown',
            'gender': 'Female',
            'birth_date': timezone.now().date() - timedelta(days=365*14),
            'birthplace': 'Town Clinic',
            'residential_address': '123 Oak St, City',
            'registered_address': '456 Pine St, Suburb',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '2.jpg',
            'leaving_date': timezone.now().date() - timedelta(days=365),
        },
        {
            'pesel': '34567890123',
            'first_name': 'Michael',
            'second_name': 'John',
            'surname': 'Smith',
            'gender': 'Male',
            'birth_date': timezone.now().date() - timedelta(days=365*12),
            'birthplace': 'City Hospital',
            'residential_address': '789 Pine St, Town',
            'registered_address': '123 Elm St, Village',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '3.jpg',
            'leaving_date': timezone.now().date() - timedelta(days=365),
        },
        {
            'pesel': '45678901234',
            'first_name': 'Olivia',
            'second_name': 'Sophia',
            'surname': 'Johnson',
            'gender': 'Female',
            'birth_date': timezone.now().date() - timedelta(days=365*11),
            'birthplace': 'Town Clinic',
            'residential_address': '456 Oak St, City',
            'registered_address': '789 Pine St, Suburb',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '4.jpg',
            'leaving_date': timezone.now().date() - timedelta(days=365),
        },
        {
            'pesel': '56789012345',
            'first_name': 'James',
            'second_name': '',
            'surname': 'Williams',
            'gender': 'Male',
            'birth_date': timezone.now().date() - timedelta(days=365*10),
            'birthplace': 'City Hospital',
            'residential_address': '123 Elm St, Town',
            'registered_address': '456 Oak St, Village',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '',
            'leaving_date': timezone.now().date() - timedelta(days=365),
        },
        {
            'pesel': '67890123456',
            'first_name': 'Charlotte',
            'second_name': 'Emma',
            'surname': 'Jones',
            'gender': 'Female',
            'birth_date': timezone.now().date() - timedelta(days=365*9),
            'birthplace': 'Town Clinic',
            'residential_address': '789 Pine St, City',
            'registered_address': '123 Oak St, Suburb',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '6.jpg',
            'leaving_date': timezone.now().date() - timedelta(days=365),
        },
        {
            'pesel': '78901234567',
            'first_name': 'Liam',
            'second_name': 'Mason',
            'surname': 'Brown',
            'gender': 'Male',
            'birth_date': timezone.now().date() - timedelta(days=365*8),
            'birthplace': 'City Hospital',
            'residential_address': '456 Oak St, Town',
            'registered_address': '789 Pine St, Village',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '7.jpg',
            'leaving_date': timezone.now().date() - timedelta(days=365),
        },
        {
            'pesel': '89012345678',
            'first_name': 'Ava',
            'second_name': 'Isabella',
            'surname': 'Taylor',
            'gender': 'Female',
            'birth_date': timezone.now().date() - timedelta(days=365*7),
            'birthplace': 'Town Clinic',
            'residential_address': '123 Elm St, City',
            'registered_address': '456 Oak St, Suburb',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '',
            'leaving_date': timezone.now().date() - timedelta(days=365),
        },
        {
            'pesel': '90123456789',
            'first_name': 'Noah',
            'second_name': 'Ethan',
            'surname': 'Martinez',
            'gender': 'Male',
            'birth_date': timezone.now().date() - timedelta(days=365*6),
            'birthplace': 'City Hospital',
            'residential_address': '789 Pine St, Town',
            'registered_address': '123 Elm St, Village',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '9.jpg',
            'leaving_date': timezone.now().date() - timedelta(days=365),
        },
        {
            'pesel': '01234567890',
            'first_name': 'Sophia',
            'second_name': 'Mia',
            'surname': 'Garcia',
            'gender': 'Female',
            'birth_date': timezone.now().date() - timedelta(days=365*5),
            'birthplace': 'Town Clinic',
            'residential_address': '456 Oak St, City',
            'registered_address': '789 Pine St, Suburb',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '10.jpg',
            'leaving_date': timezone.now().date() - timedelta(days=365),
        },
        {
            'pesel': '12345678902',
            'first_name': 'Alice',
            'second_name': 'Jane',
            'surname': 'Doe',
            'gender': 'Female',
            'birth_date': timezone.now().date() - timedelta(days=365*13),
            'birthplace': 'City Hospital',
            'residential_address': '456 Elm St, Town',
            'registered_address': '789 Oak St, Village',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '11.jpg',
        },
        {
            'pesel': '23456789012',
            'first_name': 'Emily',
            'second_name': 'Grace',
            'surname': 'Brown',
            'gender': 'Female',
            'birth_date': timezone.now().date() - timedelta(days=365*14),
            'birthplace': 'Town Clinic',
            'residential_address': '123 Oak St, City',
            'registered_address': '456 Pine St, Suburb',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '',
        },
        {
            'pesel': '34567890124',
            'first_name': 'Michael',
            'second_name': 'John',
            'surname': 'Smith',
            'gender': 'Male',
            'birth_date': timezone.now().date() - timedelta(days=365*12),
            'birthplace': 'City Hospital',
            'residential_address': '789 Pine St, Town',
            'registered_address': '123 Elm St, Village',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '13.jpg',
        },
        {
            'pesel': '45678901235',
            'first_name': 'Olivia',
            'second_name': 'Sophia',
            'surname': 'Johnson',
            'gender': 'Female',
            'birth_date': timezone.now().date() - timedelta(days=365*11),
            'birthplace': 'Town Clinic',
            'residential_address': '456 Oak St, City',
            'registered_address': '789 Pine St, Suburb',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '14.jpg',
        },
        {
            'pesel': '56789012346',
            'first_name': 'James',
            'second_name': '',
            'surname': 'Williams',
            'gender': 'Male',
            'birth_date': timezone.now().date() - timedelta(days=365*10),
            'birthplace': 'City Hospital',
            'residential_address': '123 Elm St, Town',
            'registered_address': '456 Oak St, Village',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '',
        },
        {
            'pesel': '67890123457',
            'first_name': 'Charlotte',
            'second_name': 'Emma',
            'surname': 'Jones',
            'gender': 'Female',
            'birth_date': timezone.now().date() - timedelta(days=365*9),
            'birthplace': 'Town Clinic',
            'residential_address': '789 Pine St, City',
            'registered_address': '123 Oak St, Suburb',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '16.jpg',
        },
        {
            'pesel': '78901234568',
            'first_name': 'Liam',
            'second_name': 'Mason',
            'surname': 'Brown',
            'gender': 'Male',
            'birth_date': timezone.now().date() - timedelta(days=365*8),
            'birthplace': 'City Hospital',
            'residential_address': '456 Oak St, Town',
            'registered_address': '789 Pine St, Village',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '17.jpg',
        },
        {
            'pesel': '89012345679',
            'first_name': 'Ava',
            'second_name': 'Isabella',
            'surname': 'Taylor',
            'gender': 'Female',
            'birth_date': timezone.now().date() - timedelta(days=365*7),
            'birthplace': 'Town Clinic',
            'residential_address': '123 Elm St, City',
            'registered_address': '456 Oak St, Suburb',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '18.jpg',
        },
        {
            'pesel': '90123456790',
            'first_name': 'Noah',
            'second_name': '',
            'surname': 'Martinez',
            'gender': 'Male',
            'birth_date': timezone.now().date() - timedelta(days=365*6),
            'birthplace': 'City Hospital',
            'residential_address': '789 Pine St, Town',
            'registered_address': '123 Elm St, Village',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '19.jpg',
        },
        {
            'pesel': '01234567891',
            'first_name': 'Sophia',
            'second_name': 'Mia',
            'surname': 'Garcia',
            'gender': 'Female',
            'birth_date': timezone.now().date() - timedelta(days=365*5),
            'birthplace': 'Town Clinic',
            'residential_address': '456 Oak St, City',
            'registered_address': '789 Pine St, Suburb',
            'admission_date': timezone.now().date() - timedelta(days=365*2),
            'photo_path': '20.jpg',
        },
    ]

    relatives = Relatives.objects.bulk_create(Relatives(**data) for data in relatives_data)

    children = Children.objects.bulk_create(Children(**data) for data in children_data)

    children = Children.objects.all()

    notes_data = [
        {
            'child_id': Children.objects.first(),
            'title': 'Health Note',
            'contents': 'Allergic to peanuts.'
        },
        {
            'child_id': Children.objects.first(),
            'title': 'Behavior Note',
            'contents': 'Requires extra attention in class.'
        },
        {
            'child_id': Children.objects.all()[1],
            'title': 'Diet Note',
            'contents': 'Vegetarian diet preferred.'
        },
        {
            'child_id': Children.objects.all()[2],
            'title': 'Learning Note',
            'contents': 'Excels in mathematics.'
        },
        {
            'child_id': Children.objects.all()[6],
            'title': 'Health Note',
            'contents': 'Asthma condition, keep inhaler nearby.'
        },
        {
            'child_id': Children.objects.all()[7],
            'title': 'Behavior Note',
            'contents': 'Has difficulty focusing during lessons.'
        },
        {
            'child_id': Children.objects.all()[11],
            'title': 'Health Note',
            'contents': 'Needs regular checkups for dental hygiene.'
        },
        {
            'child_id': Children.objects.all()[12],
            'title': 'Behavior Note',
            'contents': 'Responds well to positive reinforcement.'
        },
        {
            'child_id': Children.objects.all()[12],
            'title': 'Learning Note',
            'contents': 'Expresses interest in arts and crafts.'
        },
        {
            'child_id': Children.objects.all()[17],
            'title': 'Health Note',
            'contents': 'Mild allergy to strawberries.'
        },
    ]

    users_data = [
        {
            "email": "admin@admin.com",
            "first_name": "admin",
            "surname": "admin",
            "password": "pbkdf2_sha256$720000$stf4tCtVV21l2Ok6wHC3jL$ORQh/WrEoW8PKwJUuFH3AMZHQjTALZl9SS1ykrLUoM8="
        }
    ]

    Notes.objects.bulk_create(Notes(**data) for data in notes_data)
    Users.objects.bulk_create(Users(**data) for data in users_data)

    children[0].relatives.add(relatives[0])
    children[1].relatives.add(relatives[1], relatives[2])
    children[2].relatives.add(relatives[3])
    children[3].relatives.add(relatives[4], relatives[5])
    children[4].relatives.add(relatives[6])
    children[5].relatives.add(relatives[7])
    children[6].relatives.add(relatives[0])
    children[7].relatives.add(relatives[1])
    children[8].relatives.add(relatives[2])
    children[9].relatives.add(relatives[3])
    children[10].relatives.add(relatives[4])
    children[11].relatives.add(relatives[5])
    children[12].relatives.add(relatives[6])
    children[13].relatives.add(relatives[7])
    children[14].relatives.add(relatives[0])
    children[15].relatives.add(relatives[1])
    children[16].relatives.add(relatives[2])
    children[17].relatives.add(relatives[3])
    children[18].relatives.add(relatives[4])
    children[19].relatives.add(relatives[5])

