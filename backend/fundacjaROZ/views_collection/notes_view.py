import time
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import *
from rest_framework import status
from ..serializers import *





class ChildrenNotesAPIView(APIView):
    def get(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        notes = Notes.objects.filter(child_id=child)
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        child = get_object_or_404(Children, pk=pk)
        serializer = NotesSerializer(data=request.data)
        serializer.initial_data['child_id'] = child.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)










class ChildrenNotesDetailsAPIView(APIView):
    def delete(self, request, pk=None, note_id=None):
        child = get_object_or_404(Children, pk=pk)
        try:
            note = Notes.objects.get(id=note_id)
            if note.child_id == child:
                note.delete()
        except Notes.DoesNotExist:
            return Response({'error': 'Notatka nie istnieje'}, status=status.HTTP_404_NOT_FOUND)      
        return Response({'success': 'Notatka została pomyślnie usunięta'}, status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, note_id):
        child = get_object_or_404(Children, pk=pk)
        note = get_object_or_404(Notes, pk=note_id, child_id=child.id)
        serializer = NotesSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
            
            

    
            