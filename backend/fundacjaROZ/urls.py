from django.urls import path
# from .views import *
from .views_collection.children_view import CurrentChildrenAPIView,ArchivalChildrenAPIView
from .views_collection.documents_view import ChildrenDocumentsAPIView,ChildrenDocumentsDetailsAPIView
from .views_collection.notes_view import ChildrenNotesAPIView,ChildrenNotesDetailsAPIView
from .views_collection.photos_view import ChildrenPhotoAPIView
from .views_collection.relatives_view import RelativeChildrensAPIView,RelativeChildrensDetailsAPIView,ChildrenRelativesAPIView,ChildrenRelativesDetailsAPIView
from .views_collection.schools_view import ChildrenSchoolsAPIView,ChildrenSchoolsDetailsAPIView
from .views_collection.user_view import UserRegistrationAPIView,UserLoginAPIView, UserViewAPI


urlpatterns = [
	path('register/', UserRegistrationAPIView.as_view()),
	path('login/', UserLoginAPIView.as_view()),
	path('user/', UserViewAPI.as_view()),
    
	path('children/current/', CurrentChildrenAPIView.as_view()),
    path('children/archival/', ArchivalChildrenAPIView.as_view()),
    
 	path('children/<int:pk>/relatives/', ChildrenRelativesAPIView.as_view()),
    path('children/<int:pk>/relatives/<int:relative_id>/', ChildrenRelativesDetailsAPIView.as_view()),
    
    path('relatives/<int:pk>/children/', RelativeChildrensAPIView.as_view()),
    path('relatives/<int:pk>/children/<int:child_id>/', RelativeChildrensDetailsAPIView.as_view()),
    
    path('children/<int:pk>/schools/', ChildrenSchoolsAPIView.as_view()),
    path('children/<int:pk>/schools/<int:school_id>/', ChildrenSchoolsDetailsAPIView.as_view()),
    
    path('children/<int:pk>/notes/', ChildrenNotesAPIView.as_view()),
    path('children/<int:pk>/notes/<int:note_id>/', ChildrenNotesDetailsAPIView().as_view()),
    
	path('children/<int:pk>/documents/',  ChildrenDocumentsAPIView.as_view()),
    path('children/<int:pk>/documents/<int:document_id>/',  ChildrenDocumentsDetailsAPIView().as_view()),
    
    
	path('children/<int:pk>/photo/', ChildrenPhotoAPIView.as_view()),
]