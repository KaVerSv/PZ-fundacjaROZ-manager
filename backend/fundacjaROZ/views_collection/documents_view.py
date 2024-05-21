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

from django.http import HttpResponse
from rest_framework import status
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import tempfile
from .google_connection import google_connect

class DocumentsAPIView(APIView):
    google_connection = google_connect()
    DRIVE = google_connection.get_drive()
    
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
            file_ = request.FILES.get('file')
            if file_:
                filename = file_.name
                query = f"name='{filename}'"
                response = self.DRIVE.files().list(q=query, fields='files(id)').execute()
                files = response.get('files', [])
                if files:
                    base_name, extension = os.path.splitext(filename)
                    timestamp = int(time.time() * 1000)
                    filename = f"{base_name}_{timestamp}{extension}"

                file_metadata = {
                    'name': filename,
                    'parents': ['12IR6ctFeH_JrJv1Zzm7VFnm2ctOuui4g']
                }
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(file_.read())
                    media = MediaFileUpload(temp_file.name, mimetype='application/octet-stream', resumable=True)
                try:
                    response = self.DRIVE.files().create(body=file_metadata, media_body=media, fields='id').execute()
                    serializer.save(file_name=filename)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except HttpError as e:
                    return Response({'error': f'Wystąpił błąd podczas zapisywania pliku na dysku Google: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'error': 'Nie przekazano pliku'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChildrenDetailsDocumentsAPIView(APIView): 
    google_connection = google_connect()
    DRIVE = google_connection.get_drive()
     
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
            file_ = request.FILES.get('file')
            if file_:
                filename = file_.name
                query = f"name='{filename}'"
                response = self.DRIVE.files().list(q=query, fields='files(id)').execute()
                files = response.get('files', [])
                if files:
                    base_name, extension = os.path.splitext(filename)
                    timestamp = int(time.time() * 1000)
                    filename = f"{base_name}_{timestamp}{extension}"

                file_metadata = {
                    'name': filename,
                    'parents': ['12IR6ctFeH_JrJv1Zzm7VFnm2ctOuui4g']
                }
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(file_.read())
                    media = MediaFileUpload(temp_file.name, mimetype='application/octet-stream', resumable=True)
                try:
                    response = self.DRIVE.files().create(body=file_metadata, media_body=media, fields='id').execute()
                    serializer.save(file_name=filename, child_id = child)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except HttpError as e:
                    return Response({'error': f'Wystąpił błąd podczas zapisywania pliku na dysku Google: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'error': 'Nie przekazano pliku'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RelativesDetailsDocumentsAPIView(APIView):  
    google_connection = google_connect()
    DRIVE = google_connection.get_drive()
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
            file_ = request.FILES.get('file')
            if file_:
                filename = file_.name
                query = f"name='{filename}'"
                response = self.DRIVE.files().list(q=query, fields='files(id)').execute()
                files = response.get('files', [])
                if files:
                    base_name, extension = os.path.splitext(filename)
                    timestamp = int(time.time() * 1000)
                    filename = f"{base_name}_{timestamp}{extension}"

                file_metadata = {
                    'name': filename,
                    'parents': ['12IR6ctFeH_JrJv1Zzm7VFnm2ctOuui4g']
                }
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(file_.read())
                    media = MediaFileUpload(temp_file.name, mimetype='application/octet-stream', resumable=True)
                try:
                    response = self.DRIVE.files().create(body=file_metadata, media_body=media, fields='id').execute()
                    serializer.save(file_name=filename, relative_id = relative)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except HttpError as e:
                    return Response({'error': f'Wystąpił błąd podczas zapisywania pliku na dysku Google: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'error': 'Nie przekazano pliku'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentsDetailsAPIView(APIView):
    google_connection = google_connect()
    DRIVE = google_connection.get_drive()
    
    def get(self, request, pk):
        document = get_object_or_404(Documents, pk=pk)
        serializer = DocumentsSerializer(document)
        data = serializer.data
        data['file_name'] = f"http://localhost:8000/documents/{pk}/file/"
        return Response(data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk):
       

        document = get_object_or_404(Documents, pk=pk)
        if document and document.file_name:
            query = f"name='{document.file_name}'"
            try:
                response = self.DRIVE.files().list(q=query, fields='files(id)').execute()
                files = response.get('files', [])
                if files:
                    file_id = files[0]['id']
                    self.DRIVE.files().delete(fileId=file_id).execute()
                    document.delete()
                    return Response({'message': 'Dokument usunięty'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Plik nie został znaleziony'}, status=status.HTTP_404_NOT_FOUND)
            except HttpError as e:
                return Response({'error': f'Wystąpił błąd podczas usuwania dokumentu: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({'error': 'Dokument nie istnieje'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        document = get_object_or_404(Documents, pk=pk)
        if document:
            serializer = DocumentsSerializer(document, data=request.data)
            if serializer.is_valid():
                file_ = request.FILES.get('file')
                if file_:
                    SCOPES = 'https://www.googleapis.com/auth/drive'
                    file_path_store = os.path.join(settings.GOOGLE_ROOT, 'storage.json')
                    store = file.Storage(file_path_store)
                    creds = store.get()
                    if not creds or creds.invalid:
                        file_path = os.path.join(settings.GOOGLE_ROOT, 'credentials.json')
                        flow = client.flow_from_clientsecrets(file_path, SCOPES)
                        creds = tools.run_flow(flow, store)
                    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

                    query = f"name='{document.file_name}'"
                    response = DRIVE.files().list(q=query, fields='files(id)').execute()
                    files = response.get('files', [])
                    if files:
                        file_id = files[0]['id']
                        DRIVE.files().delete(fileId=file_id).execute()

                    filename = file_.name
                    query = f"name='{filename}'"
                    response = DRIVE.files().list(q=query, fields='files(id)').execute()
                    files = response.get('files', [])
                    if files:
                        base_name, extension = os.path.splitext(filename)
                        timestamp = int(time.time() * 1000)
                        filename = f"{base_name}_{timestamp}{extension}"

                    file_metadata = {
                        'name': filename,
                        'parents': ['12IR6ctFeH_JrJv1Zzm7VFnm2ctOuui4g']
                    }
                    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                        temp_file.write(file_.read())
                        media = MediaFileUpload(temp_file.name, mimetype='application/octet-stream', resumable=True)
                    try:
                        DRIVE.files().create(body=file_metadata, media_body=media, fields='id').execute()
                        serializer.save(file_name=filename)
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    except HttpError as e:
                        return Response({'error': f'Wystąpił błąd podczas zapisywania nowego pliku na dysku Google: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return Response({'error': 'Nie przekazano pliku'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentsDetailsFileAPIView(APIView):
    google_connection = google_connect()
    DRIVE = google_connection.get_drive()
             
    def get(self, request, pk=None):
       

        document = get_object_or_404(Documents, pk=pk)
        if document:
            query = f"name='{document.file_name}'"
            try:
                response = self.DRIVE.files().list(q=query, fields='files(id)').execute()
                files = response.get('files', [])
                if not files:
                    return HttpResponse("Plik nie został znaleziony.")
                
                file_id = files[0]['id']
                request = self.DRIVE.files().get_media(fileId=file_id)
                file_content = request.execute()

                file_extension = document.file_name.split('.')[-1].lower()
                
                content_type = 'image/png'

                if file_extension == 'pdf':
                    content_type = 'application/pdf'
                elif file_extension == 'png':
                    content_type = 'image/png'
                elif file_extension in ['jpg', 'jpeg']:
                    content_type = 'image/jpeg'
                elif file_extension == 'txt':
                    content_type = 'text/plain'
                elif file_extension == 'doc':
                    content_type = 'application/msword'
                elif file_extension == 'docx':
                    content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                
                
                return HttpResponse(file_content, content_type=content_type)
            
            except HttpError as e:
                return HttpResponse(f"Wystąpił błąd podczas pobierania pliku {e}")
        else:
            return Response({'error': 'Document nie istnieje'}, status=status.HTTP_404_NOT_FOUND)