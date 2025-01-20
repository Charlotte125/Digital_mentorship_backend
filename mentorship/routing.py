# routing.py
from django.urls import path
from .chatConsumer import ChatConsumer
from .testConsumer import TestConsumer
websocket_urlpatterns = [
    # Remove the $ and make sure the trailing slash is consistent
    path('ws/chat/<str:room_id>/', ChatConsumer.as_asgi()),  # Simplified path
    path('ws/testing/', TestConsumer.as_asgi())
]
