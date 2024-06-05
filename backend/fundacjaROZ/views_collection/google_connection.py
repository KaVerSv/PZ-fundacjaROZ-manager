import os
import json
from django.conf import settings
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

class google_connect:
    
    def __init__(self):
        SCOPES = ['https://www.googleapis.com/auth/drive']
        GOOGLE_ROOT = settings.GOOGLE_ROOT
        
        # Załaduj dane uwierzytelniające z pliku storage.json
        file_path_store = os.path.join(GOOGLE_ROOT, 'storage.json')
        with open(file_path_store, 'r') as token_file:
            creds_data = json.load(token_file)
        
        # Utwórz obiekt Credentials
        creds = Credentials(
            token=creds_data['token'],
            refresh_token=creds_data.get('refresh_token'),
            token_uri=creds_data['token_uri'],
            client_id=creds_data['client_id'],
            client_secret=creds_data['client_secret'],
            scopes=creds_data['scopes']
        )
        
        # Zbuduj obiekt usługi Google Drive
        self.DRIVE = build('drive', 'v3', credentials=creds)
        
    def get_drive(self):
        return self.DRIVE
