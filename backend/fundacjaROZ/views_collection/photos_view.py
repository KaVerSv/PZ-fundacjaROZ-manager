import time
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
import os
from django.http import FileResponse
from ..models import *
from rest_framework import status
from django.conf import settings
from ..serializers import *





class ChildrenPhotoAPIView(APIView):
    def get(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        photo = child.photo_path
        if photo == "":
            photo = 'default.png'
        
        file_path = os.path.join(settings.MEDIA_ROOT, photo)
        return FileResponse(open(file_path, 'rb'), status=status.HTTP_200_OK)
        
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





