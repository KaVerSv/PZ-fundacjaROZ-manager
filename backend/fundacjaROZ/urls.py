from django.urls import path

from .views_collection.children_view import CurrentChildrenAPIView,ArchivalChildrenAPIView
from .views_collection.notes_view import ChildrenNotesAPIView,ChildrenNotesDetailsAPIView
from .views_collection.photos_view import ChildrenPhotoAPIView
from .views_collection.relatives_view import RelativeChildrensAPIView,RelativeChildrensDetailsAPIView,ChildrenRelativesAPIView,ChildrenRelativesDetailsAPIView
from .views_collection.documents_view import ChildrenDetailsDocumentsAPIView,DocumentsAPIView,DocumentsDetailsAPIView, DocumentsDetailsFileAPIView, RelativesDetailsDocumentsAPIView
from .views_collection.schools_view import ChildrenSchoolsAPIView,ChildrenSchoolsDetailsAPIView
# from .views_collection.user_view import UserRegistrationAPIView,UserLoginAPIView, UserViewAPI
from .views import GoogleLoginApi#,authenticate_google, auth_callback


urlpatterns = [
	# path('register/', UserRegistrationAPIView.as_view()),
	# path('login/', UserLoginAPIView.as_view()),
	# path('user/', UserViewAPI.as_view()),
    
	path('children/current/', CurrentChildrenAPIView.as_view()),
    path('children/archival/', ArchivalChildrenAPIView.as_view()),

    path('children/<int:pk>/photo/', ChildrenPhotoAPIView.as_view()),
    
 	path('children/<int:pk>/relatives/', ChildrenRelativesAPIView.as_view()),
    path('children/<int:pk>/relatives/<int:relative_id>/', ChildrenRelativesDetailsAPIView.as_view()),
    
	path('children/<int:pk>/schools/', ChildrenSchoolsAPIView.as_view()),
    path('children/<int:pk>/schools/<int:school_id>/', ChildrenSchoolsDetailsAPIView.as_view()),

    path('relatives/<int:pk>/children/', RelativeChildrensAPIView.as_view()),
    path('relatives/<int:pk>/children/<int:child_id>/', RelativeChildrensDetailsAPIView.as_view()),
    
    path('children/<int:pk>/schools/', ChildrenSchoolsAPIView.as_view()),
    path('children/<int:pk>/schools/<int:school_id>/', ChildrenSchoolsDetailsAPIView.as_view()),
    
    path('children/<int:pk>/notes/', ChildrenNotesAPIView.as_view()),
    path('children/<int:pk>/notes/<int:note_id>/', ChildrenNotesDetailsAPIView().as_view()),
    
	path('children/<int:pk>/documents/',  ChildrenDetailsDocumentsAPIView.as_view()),
    path('relatives/<int:pk>/documents/',  RelativesDetailsDocumentsAPIView.as_view()),

    path('documents/',  DocumentsAPIView.as_view()),
    path('documents/<int:pk>/',  DocumentsDetailsAPIView.as_view()),
    path('documents/<int:pk>/file/',  DocumentsDetailsFileAPIView().as_view()),
    
    # path('auth/google/', authenticate_google, name='authenticate_google'),
    # path('auth/google/callback/', auth_callback, name='auth_callback'),

    path("api/auth/google/", GoogleLoginApi.as_view(), name="login-with-google"),

]