from django.apps import AppConfig


class FundacjarozConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fundacjaROZ'

# W pliku np. manage.py, apps.py, lub innym odpowiednim miejscu
from fixtures import add_example_data

# Wywołanie funkcji do dodawania przykładowych danych
add_example_data()
