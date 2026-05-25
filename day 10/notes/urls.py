from django.urls import path
from .views import NoteAPI

urlpatterns = [
    path('notes/', NoteAPI.as_view())
]