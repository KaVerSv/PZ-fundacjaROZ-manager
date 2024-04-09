from django.urls import path
from .views import  RelativesAPIView, RelativeDetailAPIView, UserRegistrationAPIView, UserLoginAPIView, UserViewAPI, UserLogoutViewAPI


urlpatterns = [
	path('api/user/register/', UserRegistrationAPIView.as_view()),
	path('api/user/login/', UserLoginAPIView.as_view()),
	path('api/user/', UserViewAPI.as_view()),
	path('api/user/logout/', UserLogoutViewAPI.as_view()),
    
	# path('children/current/', CurrentChildrenAPIView.as_view(), name='current-children'),
    # path('children/archival/', ArchivalChildrenAPIView.as_view(), name='archival-children'),
    
    path('relatives/', RelativesAPIView.as_view()),
    path('relatives/<int:pk>/', RelativeDetailAPIView.as_view()),
]