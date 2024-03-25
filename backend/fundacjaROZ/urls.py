from django.urls import path
from fundacjaROZ.views import UserRegistrationAPIView, UserLoginAPIView, UserViewAPI, UserLogoutViewAPI

urlpatterns = [
	path('api/user/register/', UserRegistrationAPIView.as_view()),
	path('api/user/login/', UserLoginAPIView.as_view()),
	path('api/user/', UserViewAPI.as_view()),
	path('api/user/logout/', UserLogoutViewAPI.as_view()),
]