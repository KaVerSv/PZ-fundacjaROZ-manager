from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from ..serializers import *     
        
class SchoolsAPIView(ModelViewSet):
    queryset = Schools.objects.all()
    serializer_class = SchoolsSerializer

    http_method_names = ['get', 'post', 'put', 'delete']
    
    def delete(self, request, pk=None):
        school = self.get_object()
        school.delete()
        return Response({'message': 'School deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):    
        try:
            queryset = self.filter_queryset(self.get_queryset())
            schools = queryset.all()

            serializer = self.get_serializer(schools, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Schools.DoesNotExist:
            return Response({"error": "Schools not found"}, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):        
        try:
            school = self.get_object()
            
            serializer = self.get_serializer(school)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Schools.DoesNotExist:
            return Response({"error": "Child not found"}, status=status.HTTP_404_NOT_FOUND)
 
    def create(self, request):
        serializer = SchoolsSerializer(data=request.data)
        if serializer.is_valid():   
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        school = self.get_object()
        serializer = SchoolsSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChildrenSchoolsAPIView(APIView):
    def get(self, request, pk):

        child = get_object_or_404(Children, pk=pk)
        schools = child.schools.all()

        serializer = ChildrenSchoolsSerializer(schools, many=True, context={'child_id': child.id})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        print(request.data)
        serializer = ChildrenSchoolsSerializer(data=request.data, context={'child_id': child.id})
            

        if serializer.is_valid():
            school_data = serializer.validated_data 
            try:
                school = Schools.objects.get(
                    name=school_data['name'],
                    address=school_data['address'],
                )
            except Schools.DoesNotExist:
                school = serializer.save()

            child.schools.add()

            start_date = self.request.data.get('start_date')
            end_date = self.request.data.get('end_date')


            Enrollment.objects.update_or_create(
                child=child,
                school=school,
                defaults={'start_date': start_date, 'end_date': end_date}
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChildrenSchoolsDetailsAPIView(APIView):
    def delete(self, request, pk=None, school_id=None):
        child = get_object_or_404(Children, pk=pk)
        school = get_object_or_404(Schools, pk=school_id)

        if school in child.schools.all():
            child.schools.remove(school)
            return Response({'success': 'Szkoła została pomyślnie usunięta'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Szkoła nie jest przypisana do tego dziecka'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk=None, school_id=None):
        child = get_object_or_404(Children, pk=pk)
        school = get_object_or_404(Schools, pk=school_id)

        if school:
            if school not in child.schools.all():
                child.schools.add(school)
                
                start_date = self.request.data.get('start_date')
                end_date = self.request.data.get('end_date')

                Enrollment.objects.update_or_create(
                    child=child,
                    school=school,
                    defaults={'start_date': start_date, 'end_date': end_date}
                )

                return Response({'success': 'Szkoła została pomyślnie zaktualizowana'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Szkoła nie jest przypisana do tego dziecka'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Szkoła nie istnieje'}, status=status.HTTP_404_NOT_FOUND)