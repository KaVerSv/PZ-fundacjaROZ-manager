import time
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
import os
from ..models import *
from rest_framework import status
from django.conf import settings
from ..serializers import *
from django.http import FileResponse



class ChildrenDocumentsAPIView(APIView):  
    def get(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        documents = Documents.objects.filter(child_id=child)
        serializer = DocumentsSerializer(documents, many=True)
        data = serializer.data
        for document_data in data:
            document_data['filename'] = f"http://localhost:8000/children/{child['id']}/document/{document_data['id']}"
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():            
            if 'file' in request.FILES:
                file = request.FILES['file']
                filename = file.name                
                if os.path.exists(os.path.join(settings.DOCUMENTS_ROOT, filename)):
                    name, extension = os.path.splitext(filename)
                    timestamp = int(time.time() * 1000)
                    filename = f"{name}_{timestamp}{extension}"

                with open(os.path.join(settings.DOCUMENTS_ROOT, filename), 'wb') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
            serializer.save(filename = filename)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  




class ChildrenDocumentsDetailsAPIView(APIView):
    def get(self, pk=None, document_id=None):
        child = get_object_or_404(Children, pk=pk)
        document = Documents.objects.filter(id=document_id)
        if document.child_id == child:
            file_path = os.path.join(settings.DOCUMENTS_ROOT, document.file_name)
            return FileResponse(open(file_path, 'rb'), status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Document nie istnieje'}, status=status.HTTP_404_NOT_FOUND)  
        
    def put(self, request, pk, document_id):
        child = get_object_or_404(Children, pk=pk)
        document = Documents.objects.filter(id=document_id)
        if document.child_id == child and document.file_name:
            file_path = os.path.join(settings.DOCUMENTS_ROOT, document.filename)
            if os.path.exists(file_path):
                os.remove(file_path)

        if 'file' in request.FILES:
            file = request.FILES['file']

            filename = file.name                
            if os.path.exists(os.path.join(settings.DOCUMENTS_ROOT, filename)):
                name, extension = os.path.splitext(filename)
                timestamp = int(time.time() * 1000)
                filename = f"{name}_{timestamp}{extension}"

            with open(os.path.join(settings.DOCUMENTS_ROOT, filename), 'wb') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            document.filename = filename
            document.save()
            return Response({'message': 'Plik dokumentu został zaktualizowany'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Nie przesłano zdjęcia'}, status=status.HTTP_400_BAD_REQUEST)