
from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils.timezone import now
import json
from mentorship.models import Message  # Import your Message model
from django.db.models import Count

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Capture the room_id from the URL
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        
        self.room_group_name = f"chat_{self.room_id}"

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group when the WebSocket disconnects
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
