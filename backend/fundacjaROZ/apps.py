from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .fixtures import add_example_data


class FundacjarozConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fundacjaROZ'

    def ready(self):
        post_migrate.connect(add_example_data, sender=self)