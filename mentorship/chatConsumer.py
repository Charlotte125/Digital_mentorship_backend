from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        

        await self.accept()

    async def receive(self,text_data):

        message = json.loads(text_data)
        message_type = message['message_type']

        if message_type == "clients":
            await self.client_message_handler(message)
        
        elif message_type == "employees":
            await self.employee_message_handler(message)

    async def disconnect(self,close_code):
        print("The Connection is closed")


    async def client_message_handler(self,data):

        message ={
            "message": "We Love Our Client",
            "data": data["message"]
        }

        await self.send(text_data=json.dumps(message))

    async def employee_message_handler(self,data):
        message ={
            "message": "We Love Our Employees",
            "data": data["message"]
        }
        
        await self.send(text_data=json.dumps(message))