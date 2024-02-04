# recognize/views.py

from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import io
import json

r = sr.Recognizer()

# recognize/views.py

from django.http import JsonResponse
from django.views import View

class VoiceRecognition(View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_command(self, command):
        # Tutaj dodaj logikę do przetwarzania komendy
        if 'dodaj notatkę' in command:
            note_content = command.replace('dodaj notatkę', '').strip()
            response_text = f"Twoja notatka to '{note_content}'"
        elif 'dodaj zamówienie' in command:
            order_details = command.replace('dodaj zamówienie', '').strip()
            response_text = f"Twoje zamówienie to '{order_details}'"
        else:
            response_text = "Nie rozpoznano komendy."

        return response_text

    def getText(self):
        with sr.Microphone() as source:
            try:
                print("slucham...")
                audio = r.listen(source, timeout=10)
                text = r.recognize_google(audio, language='pl-PL')
                return text
            except sr.UnknownValueError:
                print("Nie udało się rozpoznać. Nieznana wartość.")
            except sr.RequestError as e:
                print(f"Błąd zapytania do API rozpoznawania mowy: {e}")
            except Exception as e:
                print(f"Inny błąd: {e}")
            return None

    def get(self, request, *args, **kwargs):
        txt = self.getText()
        if txt:
            print(txt)

            response_text = self.process_command(txt.lower())
            return JsonResponse({'message': 'Voice recognition completed', 'recognized_text': response_text})

        return JsonResponse({'message': 'No voice command recognized'})

def home(request):
    return render(request, 'recognize/home.html')

def get_note_content(request):
    note_content = "Przykładowa treść notatki"
    return JsonResponse({'note_content': note_content})