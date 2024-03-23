# django-react-docker/backend/backend/views.py
import base64
import os
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from rest_framework.decorators import action

from .serializers import *

class ChildrenAPIView(ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer

    http_method_names = ['get', 'post', 'put', 'delete','path']

    def list(self, request):
        try:
            queryset = self.filter_queryset(self.get_queryset())

            # Pobierz listę dzieci
            children = queryset.all()

            # Aktualizuj ścieżki zdjęć dla każdego dziecka
            for child in children:
                child.photo_path = f"http://localhost:8000/children/{child.id}/photo"

            # Serializuj listę dzieci
            serializer = self.get_serializer(children, many=True)

            # Zwróć odpowiedź z zaktualizowanymi danymi
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Children.DoesNotExist:
            return Response({"error": "Children not found"}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        try:
            # Pobierz dziecko z bazy danych
            child = self.get_object()

            # Pobierz ścieżkę zdjęcia z bazy danych
            photo_path = child.photo_path

            # Zmień ścieżkę na adres URL
            photo_url = f"http://localhost:8000/children/{child.id}/photo"

            # Zaktualizuj ścieżkę zdjęcia w obiekcie
            child.photo_path = photo_url

            # Serializuj obiekt dziecka
            serializer = self.get_serializer(child)

            # Zwróć odpowiedź z zaktualizowanymi danymi
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Children.DoesNotExist:
            return Response({"error": "Child not found"}, status=status.HTTP_404_NOT_FOUND)
 
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            pesel = serializer.validated_data.get('pesel')
            if Children.objects.filter(pesel=pesel).exists():
                return Response({'error': 'Dziecko o podanym PESEL już istnieje.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Przetworzenie przesłanego zdjęcia i zapisanie go na serwerze
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                with open(os.path.join(settings.MEDIA_ROOT, photo.name), 'wb') as destination:
                    for chunk in photo.chunks():
                        destination.write(chunk)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['get'], detail=False, url_path='current', url_name='current')
    def current(self, request, *args, **kwargs):
        children = Children.objects.filter(leaving_date__isnull=True)
        serializer = ChildrenSerializer2(children, many=True)
        data = serializer.data
        for child_data in data:
            child_data['photo_path'] = f"http://localhost:8000/children/{child_data['id']}/photo"
        return Response(data, status=status.HTTP_200_OK)
    
    @action(methods=['get'], detail=False, url_path='archival', url_name='archival')
    def archival(self, request, *args, **kwargs):
        children = Children.objects.exclude(leaving_date__isnull=True)
        serializer = ChildrenSerializer2(children, many=True)
        data = serializer.data
        for child_data in data:
            child_data['photo_path'] = f"http://localhost:8000/children/{child_data['id']}/photo"
        return Response(data, status=status.HTTP_200_OK)
    
    @action(methods=['get', 'delete','put'], detail=True,url_path='photo', url_name='photo')
    def photo(self, request, pk=None):
        child = self.get_object()

        if request.method == 'GET':
            if child.photo_path:
                photo = child.photo_path
            else:
                photo = 'default.png'
            file_path = os.path.join(settings.MEDIA_ROOT, photo)
            return FileResponse(open(file_path, 'rb'), content_type='image/jpeg')
        if request.method == 'DELETE':
            if child.photo_path:
                # Usuń plik z serwera
                file_path = os.path.join(settings.MEDIA_ROOT, child.photo_path)
                if os.path.exists(file_path):
                    os.remove(file_path)
                # Ustaw wartość pola photo_path na null
                child.photo_path = None
                child.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message': 'Brak zdjęcia do usunięcia.'}, status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            # Usunięcie bieżącego zdjęcia z serwera, jeśli istnieje
            if child.photo_path:
                file_path = os.path.join(settings.MEDIA_ROOT, child.photo_path)
                if os.path.exists(file_path):
                    os.remove(file_path)

            # Przetworzenie przesłanego zdjęcia i zapisanie go na serwerze
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                with open(os.path.join(settings.MEDIA_ROOT, photo.name), 'wb') as destination:
                    for chunk in photo.chunks():
                        destination.write(chunk)
                # Ustawienie nazwy zdjęcia w bazie danych
                child.photo_path = photo.name
                child.save()
                return Response({'message': 'Zdjęcie zostało zaktualizowane'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Nie przesłano nowego zdjęcia'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(methods=['get', 'post'], detail=True, url_path='notes', url_name='notes')
    def notes(self, request, pk=None):
        child = self.get_object()

        if request.method == 'GET':
            # Pobierz wszystkie notatki dla danego dziecka
            notes = Notes.objects.filter(child_id=child)
            serializer = NotesSerializer(notes, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            # Utwórz nową notatkę dla danego dziecka
            serializer = NotesSerializer(data=request.data)
            serializer.initial_data['child_id'] = child.id
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        
    @action(methods=['put','delete'], detail=True, url_path='notes/(?P<note_id>\d+)', url_name='notes')
    def actions(self, request, pk=None, note_id=None):
        
        if request.method == 'DELETE':
            try:
                note = Notes.objects.get(id=note_id)
            except Notes.DoesNotExist:
                return Response({'error': 'Notatka nie istnieje'}, status=status.HTTP_404_NOT_FOUND)

            note.delete()
    
            return Response({'success': 'Notatka została pomyślnie usunięta'}, status=status.HTTP_204_NO_CONTENT)
        if request.method == 'PUT':

            self.serializer_class=NotesSerializer
            
            try:
                note = Notes.objects.get(id=note_id)
            except (Notes.DoesNotExist):
                return Response({'error': 'Nie znaleziono notatki'}, status=status.HTTP_404_NOT_FOUND)

            serializer = NotesSerializer(note, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    @action(methods=['get', 'delete'], detail=True, url_path='associations', url_name='associations')
    def associations(self, request, *args, **kwargs):
        if request.method == 'GET':
            child = self.get_object()
        
            # Pobierz wszystkie powiązane obiekty Association dla danego dziecka
            associations = Association.objects.filter(child_id=child)
        
            # Lista na dane powiązań z krewnymi
            associations_data = []
        
            # Iteruj przez wszystkie powiązane obiekty Association
            for association in associations:
                # Pobierz dane powiązanego krewnego
                data = RelativesSerializer1(association.relative_id).data
            
                # Dodaj informacje o typie powiązania
                data['id'] = association.id
                data['association_type'] = association.association_type
                data['relative_id'] = association.relative_id.id
                data['child_id'] = association.child_id.id
            
                # Dodaj dane do listy
                associations_data.append(data)
        
            # Zwróć dane powiązań z krewnymi
            return Response(associations_data)
        # if request.method == 'DELETE':











class RelativeAPIView(ModelViewSet):
    queryset = Relatives.objects.all()
    serializer_class = RelativesSerializer
    
    def create(self, request,*args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










class AssociationAPIView(ModelViewSet):
    queryset = Association.objects.all()
    serializer_class = AssociationSerializer
    
    def create(self, request,*args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










class NotesAPIView(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
