from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AddChildAPIView, AddRelativeAPIView,DispayChildren

router = DefaultRouter()
router.register(r'add_children', AddChildAPIView)
router.register(r'relatives', AddRelativeAPIView)
# router.register(r'child', DispayChildren, basename='child')
