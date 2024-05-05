# fixtures.py

from random import choice
from django.utils import timezone
from datetime import timedelta


def add_example_data(**kwargs):
    from .models import Relatives, Children, Notes, User, Enrollment, Schools,FamilyRelationship
    relatives_data = [
        {
            'first_name': 'John',
            'second_name': 'Doe',
            'surname': 'Smith',
            'phone_number': '123456789',
            'residential_address': '123 Main St, City',
            'e_mail': 'john.doe@example.com',
            'alive': True
        },
        {
            'first_name': 'Jan',
            'second_name': 'Andrzej',
            'surname': 'Nowak',
            'phone_number': '987654321',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'jan.nowak@example.com',
            'alive': False
        },
        {
            'first_name': 'Jan',
            'second_name': 'Paweł',
            'surname': 'Drugi',
            'phone_number': '987654333',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'jan.drugi@example.com',
            'alive': True
        },
        {
            'first_name': 'Franek',
            'second_name': '',
            'surname': 'Dolas',
            'phone_number': '999654321',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'franek.dolas@example.com',
            'alive': False
        },
        {
            'first_name': 'Piotr',
            'second_name': '',
            'surname': 'Więcek',
            'phone_number': '987333333',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'piotr.wiecek@example.com',
            'alive': True
        },
        {
            'first_name': 'Marek',
            'second_name': '',
            'surname': 'Aureliusz',
            'phone_number': '333654321',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'marek.aureliusz@example.com',
            'alive': False
        },
        {
            'first_name': 'Walenty',
            'second_name': '',
            'surname': 'Kwicoł',
            'phone_number': '987333321',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'walenty.kwicoł@example.com',
            'alive': False
        },

        {
            'first_name': 'Jądruś',
            'second_name': 'Mati',
            'surname': 'Pyzdra',
            'phone_number': '333333321',
            'residential_address': '456 Elm St, Town',
            'e_mail': 'jadrus.pyzdra@example.com',
            'alive': False
        },
    ]

    children_data = [
        {
            'pesel': '12345678901',
            'first_name': 'Alice',
            'second_name': 'Jane',
            'surname': 'Doe',
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
    User.objects.bulk_create(User(**data) for data in users_data)

    for child in children:
        mother = choice(relatives)
        father = choice(relatives)
        while mother == father: 
            father = choice(relatives)

        FamilyRelationship.objects.create(child=child, relative=mother, relation="Matka")
        FamilyRelationship.objects.create(child=child, relative=father, relation="Ojciec")

    schools_data = [
        {
            'name': 'School A',
            'address': '123 Oak St, City',
            'phone_number': '123456789',
            'e_mail': 'john.doe@example.com',
        },
        {
            'name': 'School B',
            'address': '456 Elm St, Town',
            'phone_number': '123456789',
            'e_mail': 'john.doe@example.com',
        },
        {
            'name': 'School C',
            'address': '789 Pine St, Village',
            'phone_number': '123456789',
            'e_mail': 'john.doe@example.com',
        }
    ]

    schools = Schools.objects.bulk_create(Schools(**data) for data in schools_data)

    enrollment_data = [
        {
            'child': children[0],
            'school': schools[0],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[1],
            'school': schools[0],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[2],
            'school': schools[1],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[3],
            'school': schools[1],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[4],
            'school': schools[2],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[5],
            'school': schools[2],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[6],
            'school': schools[0],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[7],
            'school': schools[0],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[8],
            'school': schools[1],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[9],
            'school': schools[1],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[10],
            'school': schools[2],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[11],
            'school': schools[2],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[12],
            'school': schools[0],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[13],
            'school': schools[0],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[14],
            'school': schools[1],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[15],
            'school': schools[1],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[16],
            'school': schools[2],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[17],
            'school': schools[2],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[18],
            'school': schools[0],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
        {
            'child': children[19],
            'school': schools[0],
            'start_date': timezone.now().date() - timedelta(days=365*2)
        },
    ]

    Enrollment.objects.bulk_create(Enrollment(**data) for data in enrollment_data)