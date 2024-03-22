# django-react-docker/backend/backend/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Children, Relatives, Association, Notes
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import action

from .serializers import ChildrenSerializer, RelativesSerializer,ChildrenSerializer2, RelativesSerializer2, AssociationSerializer, NotesSerializer

# @api_view(['GET'])
# def child(request):
#     pesel = request.GET.get('pesel')
#     if pesel:
#         try:
#             child = Children.objects.get(pesel=pesel)
#             serializer = ChildrenSerializer(child)
#             child_relatives = Relatives.objects.filter(child_pesel=pesel)
#             relatives_data = list(child_relatives.values())
#             return Response({
#                 'child': serializer.data,
#                 'child_relatives': relatives_data
#             })
#         except Children.DoesNotExist:
#             return Response({'error': 'Dziecko o podanym peselu nie zostało znalezione'}, status=404)
#     else:
#         return Response({'error': 'Brak parametru pesel'}, status=400)

# class ChildrenCurrent(ModelViewSet):
#     serializer_class = ChildrenSerializer2

#     def get_queryset(self):
#         return Children.objects.filter(leaving_date__isnull=True)

#     def create(self, request, *args, **kwargs):
#         leaving_date = request.data.get('leaving_date')
#         if leaving_date:
#             return Response({'error': 'Nie można dodać dziecka z datą opuszczenia.'}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ChildrenArchival(ModelViewSet):
#     serializer_class = ChildrenSerializer2

#     def get_queryset(self):
#         return Children.objects.exclude(leaving_date__isnull=True)

#     def create(self, request, *args, **kwargs):
#         leaving_date = request.data.get('leaving_date')
#         if leaving_date:
#             return Response({'error': 'Nie można dodać dziecka z datą opuszczenia.'}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ChildrenAPIView(ModelViewSet):
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

    @action(methods=['get','post'], detail=False, url_path='current', url_name='current')
    def current(self, request, *args, **kwargs):
        if request.method == 'GET':
            children = Children.objects.exclude(leaving_date__isnull=True)
            serializer = ChildrenSerializer2(children, many=True)
            return Response(serializer.data)

        leaving_date = request.data.get('leaving_date')
        if leaving_date:
            return Response({'error': 'Nie można dodać dziecka z datą opuszczenia.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ChildrenSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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

    @action(methods=['get'], detail=True, url_path='associations', url_name='associations')
    def associations(self, request, *args, **kwargs):
        child = self.get_object()
        
        # Pobierz wszystkie powiązane obiekty Association dla danego dziecka
        associations = Association.objects.filter(child_id=child)
        
        # Lista na dane powiązań z krewnymi
        associations_data = []
        
        # Iteruj przez wszystkie powiązane obiekty Association
        for association in associations:
            # Pobierz dane powiązanego krewnego
            relative_data = RelativesSerializer(association.relative_id).data
            
            # Dodaj informacje o typie powiązania
            relative_data['association_type'] = association.association_type
            
            # Dodaj dane do listy
            associations_data.append(relative_data)
        
        # Zwróć dane powiązań z krewnymi
        return Response(associations_data)
    
    @action(methods=['get'], detail=True, url_path='notes', url_name='notes')
    def notes(self, request, pk=None):
        child = self.get_object()

        if request.method == 'GET':
            # Pobierz wszystkie notatki dla danego dziecka
            notes = Notes.objects.filter(child_id=child)
            serializer = NotesSerializer(notes, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            # Utwórz nową notatkę dla danego dziecka
            serializer = NotesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(child_id=child)
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        
    # @action(methods=['post'], detail=True,url_path='association', url_name='association')
    # def association(self, request, *args, **kwargs):
    #     child_id = kwargs.get('child_id')
    #     associations = Association.objects.filter(child_id=child_id)
    
    #     # Pobierz identyfikatory krewnych z powiązań
    #     relatives_ids = associations.values_list('relative_id', flat=True)
    
    #     # Pobierz wszystkie informacje o krewnych na podstawie identyfikatorów
    #     relatives = Relatives.objects.filter(id__in=relatives_ids)
    
    #     # Serializuj dane krewnych i zwróć odpowiedź
    #     serializer = RelativesSerializer2(relatives, many=True)
    #     return Response(serializer.data)
        
    
class RelativeAPIView(ModelViewSet):
    queryset = Relatives.objects.all()
    serializer_class = RelativesSerializer
    
    def create(self, request,*args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AssociationAPIView(ModelViewSet):
    queryset = Association.objects.all()
    serializer_class = AssociationSerializer
    
    def create(self, request,*args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class NotesAPIView(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    
    def create(self, request,*args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
