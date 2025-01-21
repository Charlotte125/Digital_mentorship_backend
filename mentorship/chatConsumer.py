from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils.timezone import now
import json
from mentorship.models import Message  # Import your Message model
from django.db.models import Count

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        message = json.loads(text_data)
        message_type = message['message_type']

        if message_type == "clients":
            await self.client_message_handler(message)
        elif message_type == "employees":
            await self.employee_message_handler(message)

    async def disconnect(self, close_code):
        print("The Connection is closed")

    async def client_message_handler(self, data):
        # Save the message to the database
        saved_message = Message.objects.create(
            first_name=data["first_name"],  # Adjust field names as necessary
            message=data["message"],
            timestamp=now()
        )

        # Update message count
        message_count = Message.objects.filter(first_name=data["first_name"]).count()

        # Broadcast the message along with the message count
        message = {
            "first_name": saved_message.first_name,
            "message": saved_message.message,
            "timestamp": saved_message.timestamp.isoformat(),
            "message_count": message_count
        }
        await self.send(text_data=json.dumps(message))

    async def employee_message_handler(self, data):
        # Save the message to the database
        saved_message = Message.objects.create(
            first_name=data["first_name"],  # Adjust field names as necessary
            message=data["message"],
            timestamp=now()
        )

        # Update message count
        message_count = Message.objects.filter(first_name=data["first_name"]).count()

        # Broadcast the message along with the message count
        message = {
            "first_name": saved_message.first_name,
            "message": saved_message.message,
            "timestamp": saved_message.timestamp.isoformat(),
            "message_count": message_count
        }
        await self.send(text_data=json.dumps(message))
