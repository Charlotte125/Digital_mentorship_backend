from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Registration
from .serializer import RegistrationSerializer, RegistrationDetailSerializer  ,TherapistRegistartionSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 


class RegistrationAPIView(APIView):  # Renamed here
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            registration = serializer.save()  
            return Response(RegistrationSerializer(registration).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RegistrationDetailAPIView(APIView):
   def get(self, request, student_id):
    password = request.query_params.get('password')

    if not password:
        return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        registration = Registration.objects.get(student_id=student_id)

        if not check_password(password, registration.password):
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)  # Use 401 for unauthorized access

        # ... (rest of your code to serialize and return registration data)
    except Registration.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        




class TherapistregistrationAPIView(APIView):  
    def post(self, request):
        serializer = TherapistRegistartionSerializer(data=request.data)
        if serializer.is_valid():
            registration = serializer.save()  
            return Response(TherapistRegistartionSerializer(registration).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()  # Fetch all Registration objects from the database
    serializer_class = RegistrationSerializer 


     





