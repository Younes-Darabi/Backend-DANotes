from rest_framework import viewsets
# from rest_framework import permissions

from .models import Notes
from .serializers import NotesSerializer


class NotesView(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]