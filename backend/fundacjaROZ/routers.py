from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register(r'relatives', AddRelativeAPIView)

router.register(r'children', ChildrenAPIView)
# router.register(r'current', ChildrenCurrent, basename='child-current')
# router.register(r'archival', ChildrenArchival, basename='child-archival')

