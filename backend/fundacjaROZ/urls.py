from django.urls import path
from .views import  ArchivalChildrenAPIView, ChildrenRelativesAPIView, CurrentChildrenAPIView, UserRegistrationAPIView, UserLoginAPIView, UserLogoutViewAPI


urlpatterns = [
	path('register/', UserRegistrationAPIView.as_view()),
	path('login/', UserLoginAPIView.as_view()),
	# path('api/user/', UserViewAPI.as_view()),
	path('logout/', UserLogoutViewAPI.as_view()),
    
	path('children/current/', CurrentChildrenAPIView.as_view()),
    path('children/archival/', ArchivalChildrenAPIView.as_view()),
 	path('children/<int:pk>/relative/', ChildrenRelativesAPIView.as_view()),
    # path('children/<int:child_id>/relative/<int:relative_id>/', ChildrenRelativesAPIView.as_view()), 
]