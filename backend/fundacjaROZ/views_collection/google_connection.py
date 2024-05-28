from django.conf import settings
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import os

class google_connect():
    
    def __init__(self):
        SCOPES = 'https://www.googleapis.com/auth/drive'
        file_path_store = os.path.join(settings.GOOGLE_ROOT, 'storage.json')
        store = file.Storage(file_path_store)
        creds = store.get()
        if not creds or creds.invalid:
            file_path = os.path.join(settings.GOOGLE_ROOT, 'credentials.json')
            flow = client.flow_from_clientsecrets(file_path, SCOPES)
            creds = tools.run_flow(flow, store)
        self.DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
        
    def get_drive(self):
        return self.DRIVE