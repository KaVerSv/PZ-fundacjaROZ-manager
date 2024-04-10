from django.urls import path
from .views import  ArchivalChildrenAPIView, ChildrenRelativesAPIView, ChildrenRelativesDetailsAPIView, CurrentChildrenAPIView, UserRegistrationAPIView, UserLoginAPIView, UserLogoutViewAPI


urlpatterns = [
	path('register/', UserRegistrationAPIView.as_view()),
	path('login/', UserLoginAPIView.as_view()),
	# path('api/user/', UserViewAPI.as_view()),
	path('logout/', UserLogoutViewAPI.as_view()),
    
	path('children/current/', CurrentChildrenAPIView.as_view()),
    path('children/archival/', ArchivalChildrenAPIView.as_view()),
 	path('children/<int:pk>/relatives/', ChildrenRelativesAPIView.as_view()),
    path('children/<int:pk>/relatives/<int:relative_id>/', ChildrenRelativesDetailsAPIView.as_view()), 
]