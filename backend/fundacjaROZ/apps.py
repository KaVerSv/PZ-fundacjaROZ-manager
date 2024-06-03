from django.apps import AppConfig
from django.db.models.signals import post_migrate
from .fixtures import add_example_data
from django.apps import AppConfig
from django.conf import settings
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import os
import subprocess
from django.apps import AppConfig
from django.conf import settings
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file



import os
import json
from django.conf import settings
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

class FundacjarozConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fundacjaROZ'

    # def ready(self):
    #     post_migrate.connect(add_example_data, sender=self)
    # your_app/apps.py

    def ready(self):
        self.init_google_drive()


    def init_google_drive(self):
        SCOPES = ['https://www.googleapis.com/auth/drive']
        GOOGLE_ROOT = settings.GOOGLE_ROOT
        file_path_store = os.path.join(GOOGLE_ROOT, 'storage.json')

        # Sprawdzenie czy plik z danymi uwierzytelniającymi istnieje
        if os.path.exists(file_path_store):
            with open(file_path_store, 'r') as token_file:
                creds_data = json.load(token_file)

            # Utworzenie obiektu Credentials
            creds = Credentials(
                token=creds_data['token'],
                refresh_token=creds_data.get('refresh_token'),
                token_uri=creds_data['token_uri'],
                client_id=creds_data['client_id'],
                client_secret=creds_data['client_secret'],
                scopes=creds_data['scopes']
            )

            if creds and creds.valid:
                settings.GOOGLE_DRIVE_SERVICE = build('drive', 'v3', credentials=creds)
            else:
                print("Brak poświadczeń Google Drive. Uwierzytelnij się pod adresem /auth/google/")
        else:
            print("Brak pliku z danymi uwierzytelniającymi. Uwierzytelnij się pod adresem /auth/google/")

