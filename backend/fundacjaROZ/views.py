# django-react-docker/backend/backend/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Children, Relatives

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .api.serializers import ChildrenSerializer, RelativesSerializer

@api_view(['GET'])
def child(request):
    pesel = request.GET.get('pesel')
    if pesel:
        try:
            child = Children.objects.get(pesel=pesel)
            serializer = ChildrenSerializer(child)
            child_relatives = Relatives.objects.filter(child_pesel=pesel)
            relatives_data = list(child_relatives.values())
            return Response({
                'child': serializer.data,
                'child_relatives': relatives_data
            })
        except Children.DoesNotExist:
            return Response({'error': 'Dziecko o podanym peselu nie zostało znalezione'}, status=404)
    else:
        return Response({'error': 'Brak parametru pesel'}, status=400)

@api_view(['GET'])
def edit_child(request):
    return Response({
        "data": "Child edit"
    })

@api_view(['GET'])
def children(request):
    archival_children = Children.objects.exclude(leaving_date__isnull=True)
    current_children = Children.objects.filter(leaving_date__isnull=True)
    
    current_children = list(current_children.values())
    archival_children = list(archival_children.values())
    
    return Response({
        'current_children': current_children,
        'archival_children': archival_children
    })


class AddChildAPIView(APIView):
    def post(self, request):
        print(request.data)
        serializer = ChildrenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddRelativeAPIView(APIView):
    def post(self, request):
        print(request.data)
        serializer = RelativesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
