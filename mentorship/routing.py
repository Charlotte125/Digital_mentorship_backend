# routing.py
from django.urls import path
from .consumer import ChatConsumer
from .testConsumer import TestConsumer

websocket_urlpatterns = [
    path(r'ws/chat/<str:room_id>/', ChatConsumer.as_asgi()),  # Capture the room_id
    path(r'ws/testing/',TestConsumer.as_asgi())
    
]
