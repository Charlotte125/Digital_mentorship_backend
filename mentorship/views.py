from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Registration
from .serializer import RegistrationSerializer, RegistrationDetailSerializer  # Import the serializers

class RegistrationAPIView(APIView):  # Renamed here
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            registration = serializer.save()  
            return Response(RegistrationSerializer(registration).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationDetailAPIView(APIView):
    def get(self, request, student_id):
        try:
            registration = Registration.objects.get(student_id=student_id)
            serializer = RegistrationDetailSerializer(registration)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Registration.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
