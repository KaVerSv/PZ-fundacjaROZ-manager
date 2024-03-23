# django-react-docker/backend/backend/views.py
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
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

class UserCreate(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

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
    def notes1(self, request, pk=None, note_id=None):
        
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
        
    @action(methods=['get', 'post'], detail=True, url_path='relatives', url_name='relatives')
    def relatives(self, request, pk=None):
        child = self.get_object()

        if request.method == 'GET':
            # Pobierz wszystkie notatki dla danego dziecka
            relatives = child.relatives
            serializer = RelativesSerializer(relatives, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            # Utwórz nową notatkę dla danego dziecka
            serializer = RelativesSerializer(data=request.data)
            
            if serializer.is_valid():
                relative_data = serializer.validated_data  # Pobierz dane zdeserializowane

                # Sprawdź, czy obiekt Relatives już istnieje w bazie danych
                try:
                    relative = Relatives.objects.get(
                    first_name=relative_data['first_name'],
                    second_name=relative_data['second_name'],
                    surname=relative_data['surname'],
                    phone_number=relative_data['phone_number'],
                    residential_address=relative_data['residential_address'],
                    e_mail=relative_data['e_mail']
                )
                except Relatives.DoesNotExist:
                    # Jeśli obiekt Relatives nie istnieje, utwórz nowy
                    relative = serializer.save()

                # Dodaj powiązanie do dzieci
                child.relatives.add(relative)

                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        
    @action(methods=['put','delete'], detail=True, url_path='relatives/(?P<relatives_id>\d+)', url_name='relatives')
    def relatives1(self, request, pk=None, relatives_id=None):
        
        if request.method == 'DELETE':
            try:
                relative = Relatives.objects.get(id=relatives_id)
            except Relatives.DoesNotExist:
                return Response({'error': 'Rel nie istnieje'}, status=status.HTTP_404_NOT_FOUND)

            relative.delete()
    
            return Response({'success': 'Notatka została pomyślnie usunięta'}, status=status.HTTP_204_NO_CONTENT)
        if request.method == 'PUT':

            self.serializer_class=RelativesSerializer
            
            try:
                relative = Relatives.objects.get(id=relatives_id)
            except (Relatives.DoesNotExist):
                return Response({'error': 'Nie znaleziono rela'}, status=status.HTTP_404_NOT_FOUND)

            serializer = RelativesSerializer(relative, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











class RelativeAPIView(ModelViewSet):
    queryset = Relatives.objects.all()
    serializer_class = RelativesSerializer










class NotesAPIView(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
