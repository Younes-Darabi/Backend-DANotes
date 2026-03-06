from rest_framework import viewsets

from .models import Notes
from .serializers import NotesSerializer


class NotesView(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer