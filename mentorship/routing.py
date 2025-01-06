# routing.py
from django.urls import re_path
from .consumer import ChatConsumer
from .testConsumer import TestConsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_id>\d+)/$', ChatConsumer.as_asgi()),  # Capture the room_id
    re_path(r'ws/testing/',TestConsumer.as_asgi())
    
]
