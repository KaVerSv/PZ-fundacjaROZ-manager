from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'relatives', AddRelativeAPIView)

router.register(r'children', AddChildAPIView)
router.register(r'current', DispayChildrenCurrent, basename='child-current')
router.register(r'archival', DispayChildrenArchival, basename='child-archival')

