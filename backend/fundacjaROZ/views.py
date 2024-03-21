# django-react-docker/backend/backend/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Children, Relatives
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import action

from .serializers import ChildrenSerializer, RelativesSerializer,ChildrenSerializer2

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

class DispayChildrenCurrent(ModelViewSet):
    serializer_class = ChildrenSerializer2

    def get_queryset(self):
        return Children.objects.filter(leaving_date__isnull=True)

    def create(self, request, *args, **kwargs):
        leaving_date = request.data.get('leaving_date')
        if leaving_date:
            return Response({'error': 'Nie można dodać dziecka z datą opuszczenia.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DispayChildrenArchival(ModelViewSet):
    serializer_class = ChildrenSerializer2

    def get_queryset(self):
        return Children.objects.exclude(leaving_date__isnull=True)

    def create(self, request, *args, **kwargs):
        leaving_date = request.data.get('leaving_date')
        if leaving_date:
            return Response({'error': 'Nie można dodać dziecka z datą opuszczenia.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AddChildAPIView(ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer

 
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            pesel = serializer.validated_data.get('pesel')
            if Children.objects.filter(pesel=pesel).exists():
                return Response({'error': 'Dziecko o podanym PESEL już istnieje.'}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    @action(methods=['get'], detail=False,url_path='current', url_name='current')
    def current(self, request, *args, **kwargs):
        
        children = Children.objects.filter(leaving_date__isnull=True)
        serializer = ChildrenSerializer2(children, many=True)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False,url_path='archival', url_name='archival')
    def archival(self, request, *args, **kwargs):
       
        children = Children.objects.exclude(leaving_date__isnull=True)
        serializer = ChildrenSerializer2(children, many=True)
        return Response(serializer.data)
    
    @action(methods=['get','post'], detail=True,url_path='photo', url_name='photo')
    def photo(self, request, *args, **kwargs):

        child = self.get_object()
        photo_path = child.photo_path
        return Response({'photo_path': photo_path})
        

    
    
class AddRelativeAPIView(ModelViewSet):
    queryset = Relatives.objects.all()
    serializer_class = RelativesSerializer
    
    def create(self, request,*args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
