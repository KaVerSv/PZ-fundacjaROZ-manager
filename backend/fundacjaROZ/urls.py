from django.urls import path
from fundacjaROZ.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("registration/", UserCreate.as_view(), name = "registration"),
    path("api/token/", TokenObtainPairView.as_view(), name = 'token_obtain_view'),
    path("api/token/refresh/", TokenRefreshView.as_view(), name = 'token_refresh_view'),
]