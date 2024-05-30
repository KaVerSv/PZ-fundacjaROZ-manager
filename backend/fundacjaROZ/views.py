from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.conf import settings
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

class UserViewAPI(APIView):
    def get(self, request):
        user, payload = JWTAuthentication.authenticate(self, request)
        user = get_object_or_404(User, pk=user.user_id)

        user_serializer = UserRegistrationSerializer(user)
        return Response(user_serializer.data)
    
    def put(self, request, pk):
        user, payload = JWTAuthentication.authenticate(self, request)
        user = get_object_or_404(User, pk=user.user_id)
        serializer = UserRegistrationSerializer(user, data=request.data)
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
        #tu bedzie zmiana uprawnien reszte bedzie zmienial sam user
        pass
        # user = get_object_or_404(User, pk=pk)
        # serializer = UsersSerializer(user, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)