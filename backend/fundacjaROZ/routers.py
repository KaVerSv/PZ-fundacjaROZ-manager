from rest_framework.routers import DefaultRouter

from .views_collection.children_view import ChildrenAPIView
from .views_collection.relatives_view import RelativesAPIView
from .views_collection.schools_view import SchoolsAPIView

from .views_collection.user_view import UsersViewAPI

router = DefaultRouter()

router.register(r'relatives', RelativesAPIView)
router.register(r'schools', SchoolsAPIView)
router.register(r'children', ChildrenAPIView)
router.register(r'users', UsersViewAPI)


