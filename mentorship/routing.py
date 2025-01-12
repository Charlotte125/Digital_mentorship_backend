# routing.py
from django.urls import path
from .consumer import ChatConsumer
from .testConsumer import TestConsumer
websocket_urlpatterns = [
    # Remove the $ and make sure the trailing slash is consistent
    path('ws/chat/', ChatConsumer.as_asgi()),  # Simplified path
    path('ws/testing/', TestConsumer.as_asgi())
]
