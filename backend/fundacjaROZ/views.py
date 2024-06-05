import os
import json
from django.shortcuts import redirect
from django.http import HttpResponse
from django.conf import settings
from google_auth_oauthlib.flow import Flow

# Dodaj ten wiersz, aby zezwolić na niebezpieczne połączenia HTTP
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

def authenticate_google(request):
    SCOPES = ['https://www.googleapis.com/auth/drive']
    GOOGLE_ROOT = settings.GOOGLE_ROOT
    file_path = os.path.join(GOOGLE_ROOT, 'credentials.json')

    flow = Flow.from_client_secrets_file(
        file_path,
        scopes=SCOPES,
        redirect_uri='http://localhost:8000/auth/google/callback'
    )
    
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    
    request.session['state'] = state
    return redirect(authorization_url)

def auth_callback(request):
    SCOPES = ['https://www.googleapis.com/auth/drive']
    GOOGLE_ROOT = settings.GOOGLE_ROOT
    file_path = os.path.join(GOOGLE_ROOT, 'credentials.json')

    state = request.session['state']

    flow = Flow.from_client_secrets_file(
        file_path,
        scopes=SCOPES,
        state=state,
        redirect_uri='http://localhost:8000/auth/google/callback'
    )
    
    flow.fetch_token(authorization_response=request.build_absolute_uri())

    credentials = flow.credentials
    creds_data = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }
    
    file_path_store = os.path.join(GOOGLE_ROOT, 'storage.json')
    with open(file_path_store, 'w') as token_file:
        json.dump(creds_data, token_file)

    return HttpResponse("Autoryzacja zakończona pomyślnie.")