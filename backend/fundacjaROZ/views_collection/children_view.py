from rest_framework.response import Response
from rest_framework.generics import ListAPIView
import os
from ..models import Children, FamilyRelationship
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.conf import settings
from ..serializers import ChildrenSerializer, ShortChildrenSerializer

class ChildrenAPIView(ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer

    http_method_names = ['get', 'post', 'put', 'delete']
    
    def delete(self, request, pk=None):
        child = self.get_object()

        if child.photo_path:
            file_path = os.path.join(settings.MEDIA_ROOT, child.photo_path)
            if os.path.exists(file_path):
                os.remove(file_path)

        child.delete()
        return Response({'message': 'Child and associated photo deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):    
        try:
            queryset = self.filter_queryset(self.get_queryset())
            children = queryset.all()

            for child in children:
                child.photo_path = f"http://localhost:8000/children/{child.id}/photo"

            serializer = self.get_serializer(children, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Children.DoesNotExist:
            return Response({"error": "Children not found"}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):        
        try:
            child = self.get_object()
            
            photo_url = f"http://localhost:8000/children/{child.id}/photo"
            child.photo_path = photo_url
            
            serializer = self.get_serializer(child)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Children.DoesNotExist:
            return Response({"error": "Child not found"}, status=status.HTTP_404_NOT_FOUND)
 
    def create(self, request, *args, **kwargs):
        data = request.data
        if data['leaving_date'] == "":
            data['leaving_date'] = None

        serializer = ChildrenSerializer(data = data)
        if serializer.is_valid():
            pesel = serializer.validated_data.get('pesel')
            if Children.objects.filter(pesel=pesel).exists():
                return Response({'error': 'Dziecko o podanym PESEL już istnieje.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save(photo_path = "")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def update(self, request, *args, **kwargs):
        child = self.get_object()
        old_photo_path = child.photo_path
        serializer = ChildrenSerializer(child, data=request.data)

        if serializer.is_valid():
            serializer.save(photo_path = old_photo_path)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CurrentChildrenAPIView(ListAPIView):
    serializer_class = ShortChildrenSerializer

    def get_queryset(self):
        queryset = Children.objects.filter(leaving_date__isnull=True)
        first_name = self.request.query_params.get('first_name', None)
        surname = self.request.query_params.get('surname', None)
        ordering = self.request.query_params.get('ordering', 'birth_date')
        search_orphans = self.request.query_params.get('search', None)
        
        if first_name and surname:
            queryset = queryset.filter(
                first_name__icontains=first_name, surname__icontains=surname
            )
        elif first_name:
            queryset = queryset.filter(
                first_name__icontains=first_name
            )
        elif surname:
            queryset = queryset.filter(
                surname__icontains=surname
            )

        queryset = queryset.order_by(ordering)

        if search_orphans == "biological_orphans":
            orphan_child_ids = []
            for child in queryset:
                family_relationships = FamilyRelationship.objects.filter(child=child)
                mothers_exist = family_relationships.filter(relation="Matka", relative__alive=False).exists()
                fathers_exist = family_relationships.filter(relation="Ojciec", relative__alive=False).exists()
                if mothers_exist and fathers_exist:
                    orphan_child_ids.append(child.id)

        queryset = queryset.filter(id__in=orphan_child_ids)


        return queryset

    def list(self, request, *args, **kwargs):
        children = self.get_queryset()
        serializer = self.get_serializer(children, many=True)
        data = serializer.data
        for child_data in data:
            child_data['photo_path'] = f"http://localhost:8000/children/{child_data['id']}/photo"
        return Response(data, status=status.HTTP_200_OK)

class ArchivalChildrenAPIView(ListAPIView):
    serializer_class = ShortChildrenSerializer

    def get_queryset(self):
        queryset = Children.objects.exclude(leaving_date__isnull=True)
        first_name = self.request.query_params.get('first_name', None)
        surname = self.request.query_params.get('surname', None)
        ordering = self.request.query_params.get('ordering', 'birth_date')
        search_orphans = self.request.query_params.get('search', None)

        if first_name and surname:
            queryset = queryset.filter(
                first_name__icontains=first_name, surname__icontains=surname
            )
        elif first_name:
            queryset = queryset.filter(
                first_name__icontains=first_name
            )
        elif surname:
            queryset = queryset.filter(
                surname__icontains=surname
            )

        queryset = queryset.order_by(ordering)

        if search_orphans == "biological_orphans":
            orphan_child_ids = []
            for child in queryset:
                family_relationships = FamilyRelationship.objects.filter(child=child)
                mothers_exist = family_relationships.filter(relation="Matka", relative__alive=False).exists()
                fathers_exist = family_relationships.filter(relation="Ojciec", relative__alive=False).exists()
                if mothers_exist and fathers_exist:
                    orphan_child_ids.append(child.id)

        queryset = queryset.filter(id__in=orphan_child_ids)

        return queryset

    def list(self, request):
        children = self.get_queryset()
        serializer = self.get_serializer(children, many=True)
        data = serializer.data
        for child_data in data:
            child_data['photo_path'] = f"http://localhost:8000/children/{child_data['id']}/photo"
        return Response(data, status=status.HTTP_200_OK)