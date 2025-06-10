import json
import urllib.parse
from channels.generic.websocket import AsyncWebsocketConsumer

import re

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        raw_room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_name = urllib.parse.unquote(raw_room_name)

        # Sanitize para aceitar só letras, números, -, _, .
        safe_room_name = re.sub(r'[^a-zA-Z0-9_.-]', '_', self.room_name)[:99]

        self.room_group_name = f'chat_{safe_room_name}'

        print(f"Conectando na sala: {self.room_group_name}")

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        user = self.scope['user']
        username = user.username if user.is_authenticated else 'Anônimo'
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'username': event['username'],
            'message': event['message']
        }))
