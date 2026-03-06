
from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import NotesView

router = DefaultRouter()
router.register(r'',NotesView, basename='notes')

urlpatterns = [
    path('', include(router.urls))
]