import ssl
import tempfile
import time
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Children
from django.conf import settings

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import os

from django.http import HttpResponse
from rest_framework import status
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from .google_connection import google_connect
from googleapiclient.errors import HttpError
import time


def execute_with_retry(request, max_retries=5, backoff_factor=2):
    for attempt in range(max_retries):
        try:
            return request.execute()
        except (HttpError, ssl.SSLError) as e:
            if attempt < max_retries - 1:
                time.sleep(backoff_factor ** attempt) 
                print(backoff_factor ** attempt)
            else:
                raise e
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(backoff_factor ** attempt)  
            else:
                raise e


class ChildrenPhotoAPIView(APIView):
    google_connection = google_connect()
    DRIVE = google_connection.get_drive()

    def get(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        photo = child.photo_path or 'default.png'
        query = f"name='{photo}'"
        
        try:

            response = execute_with_retry(self.DRIVE.files().list(q=query, fields='files(id)'))

            files = response.get('files', [])
            if not files:
                return HttpResponse("Plik nie został znaleziony.")
            
            file_id = files[0]['id']
            file_content = execute_with_retry(self.DRIVE.files().get_media(fileId=file_id))
            return HttpResponse(file_content, content_type='image/png')
        
        except HttpError as e:
            print("Error")
            return HttpResponse(f"Wystąpił błąd podczas pobierania pliku {e}")

    def delete(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        if child.photo_path:
            # SCOPES = 'https://www.googleapis.com/auth/drive'
            # file_path_store = os.path.join(settings.GOOGLE_ROOT, 'storage.json')
            # store = file.Storage(file_path_store)
            # creds = store.get()
            # if not creds or creds.invalid:
            #     file_path = os.path.join(settings.GOOGLE_ROOT, 'credentials.json')
            #     flow = client.flow_from_clientsecrets(file_path, SCOPES)
            #     creds = tools.run_flow(flow, store)
            # DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

            query = f"name='{child.photo_path}'"
            try:
                response = self.DRIVE.files().list(q=query, fields='files(id)').execute()
                files = response.get('files', [])
                if files:
                    file_id = files[0]['id']
                    self.DRIVE.files().delete(fileId=file_id).execute()
                    
            except HttpError as e:
                return Response({'error': f'Wystąpił błąd podczas usuwania zdjecia: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
            
            child.photo_path = ""
            child.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'Brak zdjęcia do usunięcia.'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        if 'photo' in request.FILES:
            # SCOPES = 'https://www.googleapis.com/auth/drive'
            # file_path_store = os.path.join(settings.GOOGLE_ROOT, 'storage.json')
            # store = file.Storage(file_path_store)
            # creds = store.get()
            # if not creds or creds.invalid:
            #     file_path = os.path.join(settings.GOOGLE_ROOT, 'credentials.json')
            #     flow = client.flow_from_clientsecrets(file_path, SCOPES)
            #     creds = tools.run_flow(flow, store)
            # DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

            if child.photo_path:
                query = f"name='{child.photo_path}'"
                try:
                    response = self.DRIVE.files().list(q=query, fields='files(id)').execute()
                    files = response.get('files', [])
                    if files:
                        file_id = files[0]['id']
                        self.DRIVE.files().delete(fileId=file_id).execute()
                except HttpError as e:
                    return Response({'error': f'Wystąpił błąd podczas usuwania zdjecia: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
            
                child.photo_path = ""

            photo = request.FILES['photo']
            filename = photo.name   

            query = f"name='{filename}'"
            response = self.DRIVE.files().list(q=query, fields='files(id)').execute()
            files = response.get('files', [])
            if files:
                base_name, extension = os.path.splitext(filename)
                timestamp = int(time.time() * 1000)
                filename = f"{base_name}_{timestamp}{extension}"

            file_metadata = {
                'name': filename,
                'parents': ['1FOkTJQyVAXMbryg7PNDltFLLVLeQVsK6']
            }
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(photo.read())
                media = MediaFileUpload(temp_file.name, mimetype='application/octet-stream', resumable=True)
            try:
                self.DRIVE.files().create(body=file_metadata, media_body=media, fields='id').execute()
                child.photo_path = filename
                child.save()
            except:
                return Response({'error': 'Wystąpił błąd podczas zapisywania pliku na dysku Google'}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
            return Response({'message': 'Zdjęcie zostało zaktualizowane'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Nie przesłano zdjęcia'}, status=status.HTTP_400_BAD_REQUEST)