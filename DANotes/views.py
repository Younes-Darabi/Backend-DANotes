from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Notes
from .serializers import NotesSerializer

class NotesView(GenericAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

    # def get(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

