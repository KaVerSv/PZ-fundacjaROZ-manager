import time
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
import os
from ..serializers import DocumentsSerializer
from ..models import Documents, Children, Relatives
from django.conf import settings

from googleapiclient import discovery
from httplib2 import Http
from oauth2client import file, client, tools
import os

from django.http import FileResponse, HttpResponse
from rest_framework import status
from googleapiclient.errors import HttpError

class DocumentsAPIView(APIView):  
    def get(self, request):
        documents = Documents.objects.all()
        serializer = DocumentsSerializer(documents, many=True)
        data = serializer.data
        for document_data in data:
            document_data['file_name'] = f"http://localhost:8000/documents/{document_data['id']}/file/"
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            file = request.FILES.get('file')
            if file:
                filename = file.name                
                if os.path.exists(os.path.join(settings.DOCUMENTS_ROOT, filename)):
                    name, extension = os.path.splitext(filename)
                    timestamp = int(time.time() * 1000)
                    filename = f"{name}_{timestamp}{extension}"

                with open(os.path.join(settings.DOCUMENTS_ROOT, filename), 'wb') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                serializer.save(file_name=filename)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChildrenDetailsDocumentsAPIView(APIView):  
    def get(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        documents = Documents.objects.filter(child_id=child)
        serializer = DocumentsSerializer(documents, many=True)
        data = serializer.data
        for document_data in data:
            document_data['file_name'] = f"http://localhost:8000/documents/{document_data['id']}/file/"
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            file = request.FILES.get('file')
            if file:
                filename = file.name                
                if os.path.exists(os.path.join(settings.DOCUMENTS_ROOT, filename)):
                    name, extension = os.path.splitext(filename)
                    timestamp = int(time.time() * 1000)
                    filename = f"{name}_{timestamp}{extension}"

                with open(os.path.join(settings.DOCUMENTS_ROOT, filename), 'wb') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)      
            serializer.save(file_name=filename, child_id = child)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RelativesDetailsDocumentsAPIView(APIView):  
    def get(self, request, pk):
        relative = get_object_or_404(Relatives, pk=pk)
        documents = Documents.objects.filter(relative_id = relative)
        serializer = DocumentsSerializer(documents, many=True)
        data = serializer.data
        for document_data in data:
            document_data['file_name'] = f"http://localhost:8000/documents/{document_data['id']}/file/"
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        relative = get_object_or_404(Relatives, pk=pk)
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            file = request.FILES.get('file')
            if file:
                filename = file.name                
                if os.path.exists(os.path.join(settings.DOCUMENTS_ROOT, filename)):
                    name, extension = os.path.splitext(filename)
                    timestamp = int(time.time() * 1000)
                    filename = f"{name}_{timestamp}{extension}"

                with open(os.path.join(settings.DOCUMENTS_ROOT, filename), 'wb') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)    
            serializer.save(file_name=filename, relative_id = relative)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentsDetailsAPIView(APIView):
    def get(self, request, pk):
        document = get_object_or_404(Documents, pk=pk)
        serializer = DocumentsSerializer(document)
        data = serializer.data
        data['file_name'] = f"http://localhost:8000/documents/{pk}/file/"
        return Response(data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
        document = get_object_or_404(Documents, pk=pk)
        if document and document.file_name:
            file_path = os.path.join(settings.DOCUMENTS_ROOT, document.file_name)
            if os.path.exists(file_path):
                os.remove(file_path)
            document.delete()
        return Response({'message': 'Dokument usunięty'}, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        document = get_object_or_404(Documents, pk=pk)
        if document:
            filename = document.file_name
            serializer = DocumentsSerializer(document, data=request.data)

            if serializer.is_valid():
                file = request.FILES.get('file')
                if file:
                    if document.file:
                        file_path = os.path.join(settings.DOCUMENTS_ROOT, document.file)
                        if os.path.exists(file_path):
                            os.remove(file_path)
                    filename = file.name                
                    if os.path.exists(os.path.join(settings.DOCUMENTS_ROOT, filename)):
                        name, extension = os.path.splitext(filename)
                        timestamp = int(time.time() * 1000)
                        filename = f"{name}_{timestamp}{extension}"

                    with open(os.path.join(settings.DOCUMENTS_ROOT, filename), 'wb') as destination:
                        for chunk in file.chunks():
                            destination.write(chunk)    
                serializer.save(file_name = filename)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentsDetailsFileAPIView(APIView):             
    def get(self, request, pk=None):
        SCOPES = 'https://www.googleapis.com/auth/drive'
        file_path_store = os.path.join(settings.GOOGLE_ROOT, 'storage.json')
        store = file.Storage(file_path_store)
        creds = store.get()
        if not creds or creds.invalid:
            file_path = os.path.join(settings.GOOGLE_ROOT, 'credentials.json')
            flow = client.flow_from_clientsecrets(file_path, SCOPES)
            creds = tools.run_flow(flow, store)
        DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

        document = get_object_or_404(Documents, pk=pk)
        if document:
            query = f"name='{document.file_name}'"
            try:
                response = DRIVE.files().list(q=query, fields='files(id)').execute()
                files = response.get('files', [])
                if not files:
                    return HttpResponse("Plik nie został znaleziony.")
                
                file_id = files[0]['id']
                request = DRIVE.files().get_media(fileId=file_id)
                
                file_content = request.execute()
                
                file_extension = document.file_name.split('.')[-1].lower()
                content_type = 'image/png'
                
                if file_extension == 'pdf':
                    content_type = 'application/pdf'
                elif file_extension == 'png':
                    content_type = 'image/png'
                elif file_extension == 'jpg' or file_extension == 'jpeg':
                    content_type = 'image/jpeg'
                
                return HttpResponse(file_content, content_type=content_type)
            
            except HttpError as e:
                return HttpResponse(f"Wystąpił błąd podczas pobierania pliku {e}")
        else:
            return Response({'error': 'Document nie istnieje'}, status=status.HTTP_404_NOT_FOUND)