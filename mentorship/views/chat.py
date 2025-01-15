from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import ChatRoom, Message

class ChatRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        rooms = ChatRoom.objects.filter(user1=user) | ChatRoom.objects.filter(user2=user)
        return Response([{"id": room.id, "user1": room.user1.username, "user2": room.user2.username} for room in rooms])

class SendMessageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        room_id = request.data.get('room_id')
        content = request.data.get('content')

        try:
            room = ChatRoom.objects.get(id=room_id)
            message = Message.objects.create(room=room, sender=request.user, content=content)
            return Response({"success": True, "message": "Message sent."})
        except ChatRoom.DoesNotExist:
            return Response({"error": "Chat room not found."}, status=404)


class CreateRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        sender = request.user  
        receiver_username = request.data.get('receiver') 

        # Validate the second user
        try:
            receiver = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            return Response({"error": "User does not exist."}, status=404)

        # Ensure a room doesn't already exist between the two users
        room, created = ChatRoom.objects.get_or_create(
            user1=min(sender, receiver, key=lambda u: u.id), 
            user2=max(sender, receiver, key=lambda u: u.id)
        )

        if created:
            return Response({
                "success": True,
                "room_id": room.id,
                "message": "Room created successfully."
            }, status=201)
        else:
            return Response({
                "success": False,
                "room_id": room.id,
                "message": "Room already exists."
            }, status=200)