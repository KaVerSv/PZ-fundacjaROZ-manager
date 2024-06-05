# authenticate_google.py
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import os
import webbrowser
from django.conf import settings

def authenticate_google_drive():
    SCOPES = 'https://www.googleapis.com/auth/drive'
    GOOGLE_ROOT = settings.GOGGLE_ROOT  # Zastąp właściwą ścieżką
    file_path_store = os.path.join(GOOGLE_ROOT, 'storage.json')
    store = file.Storage(file_path_store)
    creds = store.get()
    
    if not creds or creds.invalid:
        file_path = os.path.join(GOOGLE_ROOT, 'credentials.json')
        flow = client.flow_from_clientsecrets(file_path, SCOPES)
        
        # Uruchomienie procesu uwierzytelniania w przeglądarce
        creds = tools.run_flow(flow, store)
        webbrowser.open(flow.step1_get_authorize_url())
        
    return creds

if __name__ == "__main__":
    authenticate_google_drive()
