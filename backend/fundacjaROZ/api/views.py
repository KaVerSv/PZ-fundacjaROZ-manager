from rest_framework.viewsets import ModelViewSet
from ..models import Children, Relatives
from .serializers import ChildrenSerializer, RelativesSerializer

class ChildrenViewSet(ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer

class RelativesViewSet(ModelViewSet):
    queryset = Relatives.objects.all()
    serializer_class = RelativesSerializer

