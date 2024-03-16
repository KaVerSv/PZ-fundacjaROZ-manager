# django-react-docker/backend/backend/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Children

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .api.serializers import ChildrenSerializer

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


class AddChildAPIView(APIView):
    def post(self, request):
        print(request.data)
        serializer = ChildrenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
