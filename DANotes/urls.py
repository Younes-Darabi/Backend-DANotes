from django.urls import path
from .views import NotesView, NoteDetailView

urlpatterns = [
    path('', NotesView.as_view()),
    path('<int:pk>/', NoteDetailView.as_view())
]