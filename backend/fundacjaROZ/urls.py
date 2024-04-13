from django.urls import path
from .views import *


urlpatterns = [
	path('register/', UserRegistrationAPIView.as_view()),
	path('login/', UserLoginAPIView.as_view()),
	path('user/', UserViewAPI.as_view()),
    
	path('children/current/', CurrentChildrenAPIView.as_view()),
    path('children/archival/', ArchivalChildrenAPIView.as_view()),
    
 	path('children/<int:pk>/relatives/', ChildrenRelativesAPIView.as_view()),
    path('children/<int:pk>/relatives/<int:relative_id>/', ChildrenRelativesDetailsAPIView.as_view()),
    
    path('children/<int:pk>/notes/', ChildrenNotesAPIView.as_view()),
    path('children/<int:pk>/notes/<int:note_id>/', ChildrenNotesDetailsAPIView().as_view()),
    
	path('children/<int:pk>/photo/', ChildrenPhotoAPIView.as_view()),
]