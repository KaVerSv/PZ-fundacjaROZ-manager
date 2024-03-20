from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'add_children', AddChildAPIView)
router.register(r'relatives', AddRelativeAPIView)
router.register(r'children/current', DispayChildrenCurrent, basename='child')
router.register(r'children/archival', DispayChildrenArchival, basename='child2')

