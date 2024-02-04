import json
from channels.generic.websocket import AsyncWebsocketConsumer
from recognize.views import VoiceRecognition

class VoiceConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

        # Tu możesz umieścić kod inicjalizacyjny, jeśli jest taki potrzebny

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Tutaj obsługujemy komunikaty od klienta (jeśli potrzebne)
        pass

    async def send_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))
