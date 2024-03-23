from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'relatives', RelativeAPIView)
router.register(r'children', ChildrenAPIView)
router.register(r'notes', NotesAPIView)