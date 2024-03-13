# django-react-docker/backend/backend/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Children

@api_view(['GET'])
def child(request):
    return Response({
        "data": "Child"
    })
    # wyślij dane z from .models import Children, Notes, Relatives, Documents do reacta

@api_view(['GET'])
def children(request):
    return Response({
        "data": "Children list from fundaction"
    })

@api_view(['GET'])
def add_child(request):
    return Response({
        "data": "Child add"
    })

@api_view(['GET'])
def edit_child(request):
    return Response({
        "data": "Child edit"
    })

@api_view(['GET'])
def children(request):
    children = Children.objects.all()
    data = list(children.values())
    return Response(data)