from django.urls import path
from .views import VoiceRecognition, home, get_note_content

urlpatterns = [
    path('voice/', VoiceRecognition.as_view(), name='voice_recognition'),
    path('home/', home, name='home'),
    path('get_note_content/', get_note_content, name='get_note_content'),  # Nowa ścieżka URL
]