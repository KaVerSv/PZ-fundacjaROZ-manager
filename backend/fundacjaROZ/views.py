from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.views import APIView
import os
from django.http import FileResponse, HttpResponse
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.conf import settings
import jwt
from rest_framework.decorators import action
from .serializers import *
from .authentication import JWTAuthentication

class UserRegistrationAPIView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_user = serializer.save()
            if new_user:
                access_token = JWTAuthentication.create_jwt(new_user)
                return Response(data={'token': access_token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginAPIView(APIView):
	serializer_class = UserLoginSerializer
	permission_classes = (AllowAny,)

	def post(self, request):
		email = request.data.get('email', None)
		user_password = request.data.get('password', None)

		if not user_password:
			raise AuthenticationFailed('A user password is needed.')

		if not email:
			raise AuthenticationFailed('An user email is needed.')

		user_instance = authenticate(username=email, password=user_password)

		if not user_instance:
			raise AuthenticationFailed('User not found.')

		if user_instance.is_active:
			access_token = JWTAuthentication.create_jwt(user_instance)
			return Response(data={'token': access_token}, status=status.HTTP_200_OK)

		return Response({
			'message': 'Something went wrong.'
		})

# class UserViewAPI(APIView):

#     def get(self, request):
#         # W tym momencie użytkownik jest już uwierzytelniony
#         authenticated_user, payload = request.user

#         # Sprawdź, czy identyfikator użytkownika z tokena JWT zgadza się z tym w żądaniu
#         if not authenticated_user.user_id:
#             return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

#         user_model = get_user_model()
#         user = user_model.objects.filter(user_id=authenticated_user.user_id).first()
#         user_serializer = UserRegistrationSerializer(user)
#         return Response(user_serializer.data)

class UserLogoutViewAPI(APIView):

	def get(self, request):
		user_token = request.COOKIES.get('access_token', None)
		if user_token:
			response = Response()
			response.delete_cookie('access_token')
			response.data = {
				'message': 'Logged out successfully.'
			}
			return response
		response = Response()
		response.data = {
			'message': 'User is already logged out.'
		}
		return response

class ChildrenAPIView(ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get', 'post', 'put', 'delete','path']
    
    def delete(self, request):
        try:
            children = Children.objects.all()
            for child in children:
                if child.photo_path:
                    file_path = os.path.join(settings.MEDIA_ROOT, child.photo_path)
                    if os.path.exists(file_path):
                        os.remove(file_path)
                child.delete()
            return Response({'message': 'All children deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self, request, pk=None):
        child = self.get_object()

        if child.photo_path:
            file_path = os.path.join(settings.MEDIA_ROOT, child.photo_path)
            if os.path.exists(file_path):
                os.remove(file_path)

        child.delete()

        return Response({'message': 'Child and associated photo deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):    
        try:
            # self.permission_classes = [IsAuthenticated]
            queryset = self.filter_queryset(self.get_queryset())

            children = queryset.all()

            for child in children:
                child.photo_path = f"http://localhost:8000/children/{child.id}/photo"

            serializer = self.get_serializer(children, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Children.DoesNotExist:
            return Response({"error": "Children not found"}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):        
        try:
            child = self.get_object()

            photo_path = child.photo_path

            photo_url = f"http://localhost:8000/children/{child.id}/photo"

            child.photo_path = photo_url

            serializer = self.get_serializer(child)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Children.DoesNotExist:
            return Response({"error": "Child not found"}, status=status.HTTP_404_NOT_FOUND)
 
    def create(self, request, *args, **kwargs):        
        # self.permission_classes = [IsAuthenticated]
        serializer = ChildrenSerializer1(data=request.data)
        if serializer.is_valid():
            pesel = serializer.validated_data.get('pesel')
            if Children.objects.filter(pesel=pesel).exists():
                return Response({'error': 'Dziecko o podanym PESEL już istnieje.'}, status=status.HTTP_400_BAD_REQUEST)
            
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                with open(os.path.join(settings.MEDIA_ROOT, photo.name), 'wb') as destination:
                    for chunk in photo.chunks():
                        destination.write(chunk)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    @action(methods=['get', 'delete','put'], detail=True,url_path='photo', url_name='photo')
    def photo(self, request, pk=None):        
        child = self.get_object()

        if request.method == 'GET':
            if child.photo_path:
                photo = child.photo_path
            else:
                photo = 'default.png'
            file_path = os.path.join(settings.MEDIA_ROOT, photo)
            if photo.lower().endswith(('.png', '.jpg', '.jpeg')):
                content_type = 'image/jpeg' if photo.lower().endswith(('.jpg', '.jpeg')) else 'image/png'
                return FileResponse(open(file_path, 'rb'), content_type=content_type)
            else:
                return HttpResponse("Unsupported file format", status=400)
        if request.method == 'DELETE':
            if child.photo_path:
                file_path = os.path.join(settings.MEDIA_ROOT, child.photo_path)
                if os.path.exists(file_path):
                    os.remove(file_path)
                child.photo_path = None
                child.save()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message': 'Brak zdjęcia do usunięcia.'}, status=status.HTTP_404_NOT_FOUND)
        if request.method == 'PUT':
            if child.photo_path:
                file_path = os.path.join(settings.MEDIA_ROOT, child.photo_path)
                if os.path.exists(file_path):
                    os.remove(file_path)

            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                
                if hasattr(photo, 'content_type') and photo.content_type in ['image/jpeg', 'image/png']:
                    with open(os.path.join(settings.MEDIA_ROOT, photo.name), 'wb') as destination:
                        for chunk in photo.chunks():
                            destination.write(chunk)
                    child.photo_path = photo.name
                    child.save()
                    return Response({'message': 'Zdjęcie zostało zaktualizowane'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Nieobsługiwany typ pliku'}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
            else:
                return Response({'error': 'Nie przesłano zdjęcia'}, status=status.HTTP_400_BAD_REQUEST)


    
    @action(methods=['get', 'post'], detail=True, url_path='notes', url_name='notes')
    def notes(self, request, pk=None):        
        child = self.get_object()

        if request.method == 'GET':
            notes = Notes.objects.filter(child_id=child)
            serializer = NotesSerializer(notes, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
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

class ChildrenRelativesAPIView(CreateAPIView, ListAPIView, DestroyAPIView):
    def get(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        relatives = child.relatives.all()
        serializer = RelativesSerializer(relatives, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        serializer = RelativesSerializer(data=request.data)
            
        if serializer.is_valid():
            relative_data = serializer.validated_data 

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
                relative = serializer.save()

            child.relatives.add(relative)

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    # def delete(self, request, child_id=None, relative_id=None):
    #     child = get_object_or_404(Children, pk=child_id)
    #     relative = get_object_or_404(Relatives, pk=relative_id)

    #     if relative in child.relatives.all():
    #         child.relatives.remove(relative)
    #         return Response({'success': 'Krewny został pomyślnie usunięty'}, status=status.HTTP_204_NO_CONTENT)
    #     else:
    #         return Response({'error': 'Krewny nie jest przypisany do tego dziecka'}, status=status.HTTP_404_NOT_FOUND)









class CurrentChildrenAPIView(ListAPIView):
    queryset = Children.objects.filter(leaving_date__isnull=True)
    serializer_class = ChildrenSerializer2

    def list(self, request, *args, **kwargs):
        children = self.get_queryset()
        serializer = self.get_serializer(children, many=True)
        data = serializer.data
        for child_data in data:
            child_data['photo_path'] = f"http://localhost:8000/children/{child_data['id']}/photo"
        return Response(data, status=status.HTTP_200_OK)










class ArchivalChildrenAPIView(ListAPIView):
    queryset = Children.objects.exclude(leaving_date__isnull=True)
    serializer_class = ChildrenSerializer2

    def list(self, request):
        children = self.get_queryset()
        serializer = self.get_serializer(children, many=True)
        data = serializer.data
        for child_data in data:
            child_data['photo_path'] = f"http://localhost:8000/children/{child_data['id']}/photo"
        return Response(data, status=status.HTTP_200_OK)










class RelativesAPIView(ModelViewSet):
    queryset = Relatives.objects.all()
    serializer_class = RelativesSerializer
     
    http_method_names = ['get', 'post', 'delete', 'put']
    
    def destroy(self, request, pk):
        relative = get_object_or_404(Relatives, pk=pk)
        relative.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        serializer = RelativesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):   
        relatives = Relatives.objects.all()
        serializer = RelativesSerializer(relatives, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):    
        relative = get_object_or_404(Relatives, pk=pk)
        serializer = RelativesSerializer(relative)
        return Response(serializer.data)
    
    def update(self, request, pk):
        relative = get_object_or_404(Relatives, pk=pk)
        serializer = RelativesSerializer(relative, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










class UsersViewAPI(ModelViewSet): 
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
     
    http_method_names = ['get', 'post', 'delete', 'put']

    def destroy(self, request, pk):
        user, payload = JWTAuthentication.authenticate(self, request)
        print(payload.get('user_id'))

        if int(pk) == payload.get('user_id'):
            return Response({'error': 'Cannot delete currently logged in user'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(User, pk=pk)
        user.delete()  
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):    
        queryset = self.filter_queryset(self.get_queryset())
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
