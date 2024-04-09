from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
import os
from django.http import FileResponse, HttpResponse
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.conf import settings
from .utils import generate_access_token
import jwt
from rest_framework.decorators import action
from .serializers import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
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

class UserViewAPI(APIView):

	def get(self, request):
		user_token = request.COOKIES.get('access_token')

		if not user_token:
			raise AuthenticationFailed('Unauthenticated user.')

		payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])

		user_model = get_user_model()
		user = user_model.objects.filter(user_id=payload['user_id']).first()
		user_serializer = UserRegistrationSerializer(user)
		return Response(user_serializer.data)
     
class UsersViewAPI(ModelViewSet):
     
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
     
    http_method_names = ['get', 'post', 'delete', 'put']

    def is_valid_token(token):
        try:
            decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=['HS256'])
            
            user_id = decoded_token['user_id']
            user = User.objects.get(pk=user_id)
            
            # Tutaj możesz dodać dodatkowe sprawdzenia, np. czy konto użytkownika jest aktywne itp.
            
            return True
        except jwt.ExpiredSignatureError:
            # Obsługa wyjątku, gdy token wygasł
            return False
        except (jwt.InvalidTokenError, User.DoesNotExist):
            # Obsługa innych błędów związanych z tokenem lub użytkownikiem
            return False
    
    def dispatch(self, request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if auth_header:
            user_token = auth_header.split(' ')[1]
            
            if not self.is_valid_token(user_token):
                raise AuthenticationFailed('Unauthenticated user.')
        return super().dispatch(request, *args, **kwargs)
    
    def delete(self, request):
        users = User.objects.all()

        user_token = request.COOKIES.get('access_token')
        payload = jwt.decode(user_token, settings.SECRET_KEY, algorithms=['HS256'])

        for user in users:
            if user.user_id != payload['user_id']:
                user.delete()
        return Response({'message': 'All relatives deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):    
        try:
            queryset = self.filter_queryset(self.get_queryset())

            serializer = UsersSerializer(queryset, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Children.DoesNotExist:
            return Response({"error": "Children not found"}, status=status.HTTP_404_NOT_FOUND)

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
    
    @action(methods=['get'], detail=False, url_path='current', url_name='current')
    # @authentication_classes([SessionAuthentication, BasicAuthentication])
    # @permission_classes([IsAuthenticated])
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
        
    @action(methods=['get', 'post'], detail=True, url_path='relatives', url_name='relatives')
    def relatives(self, request, pk=None):       
        child = self.get_object()

        if request.method == 'GET':
            relatives = child.relatives
            serializer = RelativesSerializer(relatives, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
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


# class CurrentChildrenAPIView(APIView):
#     def get(self, request):
#         children = Children.objects.filter(leaving_date__isnull=True)
#         serializer = ChildrenSerializer2(children, many=True)
#         data = serializer.data
#         for child_data in data:
#             child_data['photo_path'] = f"http://localhost:8000/children/{child_data['id']}/photo"
#         return Response(data, status=status.HTTP_200_OK)

class ArchivalChildrenAPIView(APIView):
    def get(self, request):    
        children = Children.objects.exclude(leaving_date__isnull=True)
        serializer = ChildrenSerializer2(children, many=True)
        data = serializer.data
        print(data)
        for child_data in data:
            child_data['photo_path'] = f"http://localhost:8000/children/{child_data['id']}/photo"
        return Response(data, status=status.HTTP_200_OK)





  
class RelativesAPIView(APIView):
    def get(self, request):
        relatives = Relatives.objects.all()
        serializer = RelativesSerializer(relatives, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RelativesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RelativeDetailAPIView(APIView):
    def get(self, request, pk):
        relative = get_object_or_404(Relatives, pk=pk)
        serializer = RelativesSerializer(relative)
        return Response(serializer.data)
    
    def put(self, request, pk):
        relative = get_object_or_404(Relatives, pk=pk)
        serializer = RelativesSerializer(relative, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        relative = get_object_or_404(Relatives, pk=pk)
        relative.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)