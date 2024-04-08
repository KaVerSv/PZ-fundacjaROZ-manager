from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ChildrenViewSet, RelativesViewSet

post_router = DefaultRouter()
post_router.register(r'children', ChildrenViewSet)
post_router.register(r'relatives', RelativesViewSet)