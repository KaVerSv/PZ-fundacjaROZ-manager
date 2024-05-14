import time
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from ..models import Children
from rest_framework import status
from django.conf import settings

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import os

from django.http import HttpResponse
from rest_framework import status
from googleapiclient.errors import HttpError

class ChildrenPhotoAPIView(APIView):
    # def get(self, request, pk):
    #     child = get_object_or_404(Children, pk=pk)
    #     photo = child.photo_path
    #     if photo == "":
    #         photo = 'default.png'
        
    #     file_path = os.path.join(settings.MEDIA_ROOT, photo)
    #     return FileResponse(open(file_path, 'rb'), status=status.HTTP_200_OK)
    def get(self, request, pk):
        SCOPES = 'https://www.googleapis.com/auth/drive'
        file_path_store = os.path.join(settings.GOOGLE_ROOT, 'storage.json')
        store = file.Storage(file_path_store)
        creds = store.get()
        if not creds or creds.invalid:
            file_path = os.path.join(settings.GOOGLE_ROOT, 'credentials.json')
            flow = client.flow_from_clientsecrets(file_path, SCOPES)
            creds = tools.run_flow(flow, store)
        DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

        child = get_object_or_404(Children, pk=pk)
        photo = child.photo_path

        if not photo:
            photo = 'default.png'

        query = f"name='{photo}'"
        try:
            response = DRIVE.files().list(q=query, fields='files(id)').execute()
            files = response.get('files', [])
            if not files:
                return HttpResponse("Plik nie został znaleziony.")
            
            file_id = files[0]['id']
            request = DRIVE.files().get_media(fileId=file_id)
            
            file_content = request.execute()
            
            return HttpResponse(file_content, content_type='image/png')
        
        except HttpError as e:
            return HttpResponse(f"Wystąpił błąd podczas pobierania pliku {e}")


    def delete(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        if child.photo_path:
            file_path = os.path.join(settings.MEDIA_ROOT, child.photo_path)
            if os.path.exists(file_path):
                os.remove(file_path)
            child.photo_path = ""
            child.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'Brak zdjęcia do usunięcia.'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        if child.photo_path:
            file_path = os.path.join(settings.MEDIA_ROOT, child.photo_path)
            if os.path.exists(file_path):
                os.remove(file_path)

        if 'photo' in request.FILES:
            photo = request.FILES['photo']

            filename = photo.name                
            if os.path.exists(os.path.join(settings.MEDIA_ROOT, filename)):
                name, extension = os.path.splitext(filename)
                timestamp = int(time.time() * 1000)
                filename = f"{name}_{timestamp}{extension}"
            
            if hasattr(photo, 'content_type') and photo.content_type in ['image/jpeg', 'image/png']:
                with open(os.path.join(settings.MEDIA_ROOT, filename), 'wb') as destination:
                    for chunk in photo.chunks():
                        destination.write(chunk)
                child.photo_path = filename
                child.save()
                return Response({'message': 'Zdjęcie zostało zaktualizowane'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Nieobsługiwany typ pliku'}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
        else:
            return Response({'error': 'Nie przesłano zdjęcia'}, status=status.HTTP_400_BAD_REQUEST)