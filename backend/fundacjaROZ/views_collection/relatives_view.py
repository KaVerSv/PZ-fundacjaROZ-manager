from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from ..serializers import *





class RelativesAPIView(ModelViewSet):
    queryset = Relatives.objects.all()
    serializer_class = RelativesSerializer
     
    http_method_names = ['get', 'post', 'delete', 'put']
    
    def destroy(self, request, pk):
        relative = get_object_or_404(Relatives, pk=pk)
        relative.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request):
        serializer = RelativesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):   
        relatives = Relatives.objects.all()
        serializer = RelativesSerializer(relatives, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):    
        relative = get_object_or_404(Relatives, pk=pk)
        serializer = RelativesSerializer(relative)
        return Response(serializer.data)
    
    def update(self, request, pk):
        relative = get_object_or_404(Relatives, pk=pk)
        serializer = RelativesSerializer(relative, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#---------------------------- relatives/<int:pk>/children/ -----------------------------------------

class RelativeChildrensAPIView(APIView):
    def get(self, request, pk):
        
        relative = get_object_or_404(Relatives, pk=pk)
        children = Children.objects.filter(familyrelationship__relative=relative)
        
        for child in children:
            child.photo_path = f"http://localhost:8000/children/{child.id}/photo"
            
        serializer = RelativeChildrensSerializer(children, many=True, context={'relative_id': relative.id})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
#------------------------------ relatives/<int:pk>/children/<int:child_id>/  --------------------------------------------

class RelativeChildrensDetailsAPIView(APIView):
    def delete(self, request, pk=None, child_id=None):
        child = get_object_or_404(Children, pk=child_id)
        relative = get_object_or_404(Relatives, pk=pk)
        
        if relative in child.relatives.all():
            child.relatives.remove(relative)
            return Response({'success': 'Dziecka został pomyślnie usunięty'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Dziecko nie jest przypisany do tego dziecka'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk=None, child_id=None):
        child = get_object_or_404(Children, pk=child_id)
        relative = get_object_or_404(Relatives, pk=pk)

        if relative:
            if relative not in child.relatives.all():
                child.relatives.add(relative)
                
                relation = self.request.data.get('relation')

                FamilyRelationship.objects.update_or_create(
                    child=child,
                    relative=relative,
                    defaults={'relation': relation}
                )

                return Response({'success': 'Krewny został pomyślnie zaktualizowany'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Krewny nie jest przypisany do tego dziecka'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Krewny nie istnieje'}, status=status.HTTP_404_NOT_FOUND)




# ------------------------------ children/<int:pk>/relatives/ ----------------------------------

class ChildrenRelativesAPIView(APIView):
    def get(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        relatives = child.relatives.all()
        serializer = ChildrenRelativesSerializer(relatives, many=True, context={'child_id': child.id})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        serializer = ChildrenRelativesSerializer(data=request.data)
            
        if serializer.is_valid():
            relative_data = serializer.validated_data 

            try:
                relative = Relatives.objects.get(
                    first_name=relative_data['first_name'],
                    second_name=relative_data['second_name'],
                    surname=relative_data['surname'],
                    phone_number=relative_data['phone_number'],
                    residential_address=relative_data['residential_address'],
                    e_mail=relative_data['e_mail']
                )
            except Relatives.DoesNotExist:
                relative = serializer.save()

            child.relatives.add(relative)

            relation = self.request.data.get('relation')

            FamilyRelationship.objects.update_or_create(
                child=child,
                relative=relative,
                defaults={'relation': relation}
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------ children/<int:pk>/relatives/<int:relative_id>/--------------------------------------

class ChildrenRelativesDetailsAPIView(APIView):
    def delete(self, request, pk=None, relative_id=None):
        child = get_object_or_404(Children, pk=pk)
        relative = get_object_or_404(Relatives, pk=relative_id)

        if relative in child.relatives.all():
            child.relatives.remove(relative)
            return Response({'success': 'Krewny został pomyślnie usunięty'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'Krewny nie jest przypisany do tego dziecka'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk=None, relative_id=None):
        child = get_object_or_404(Children, pk=pk)
        relative = get_object_or_404(Relatives, pk=relative_id)

        if relative:
            if relative not in child.relatives.all():
                child.relatives.add(relative)
                
                relation = self.request.data.get('relation')

                FamilyRelationship.objects.update_or_create(
                    child=child,
                    relative=relative,
                    defaults={'relation': relation}
                )

                return Response({'success': 'dziecko został pomyślnie zaktualizowany'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'dziecko nie jest przypisany do tego dziecka'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'dziecko nie istnieje'}, status=status.HTTP_404_NOT_FOUND)


