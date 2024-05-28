import time
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
import os
from ..serializers import DocumentsSerializer
from ..models import Documents, Children, Relatives
from rest_framework import status
from django.conf import settings
from django.http import FileResponse

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
        document = get_object_or_404(Documents, pk=pk)
        if document:
            file_path = os.path.join(settings.DOCUMENTS_ROOT, document.file_name)
            return FileResponse(open(file_path, 'rb'), status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Document nie istnieje'}, status=status.HTTP_404_NOT_FOUND)