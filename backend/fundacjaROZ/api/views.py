from rest_framework.viewsets import ModelViewSet
from ..models import Children
from .serializers import ChildrenSerializer

class ChildrenViewSet(ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer