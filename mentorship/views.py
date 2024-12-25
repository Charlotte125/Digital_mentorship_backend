from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Registration
from .serializer import RegistrationSerializer, RegistrationDetailSerializer  ,TherapistRegistartionSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from .models import PasswordResetToken
from rest_framework.exceptions import ValidationError
from .serializer import PasswordResetSerializer  
import uuid
from datetime import datetime





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




class PasswordResetRequestAPIView(APIView):
 def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        
        if serializer.is_valid():
            email_address = serializer.validated_data.get('email_address')
            print(f"Received email address: {email_address}")  # Debugging line
            
            if not email_address:
                return Response({'message': 'Email is required.'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = User.objects.get(email__iexact=email_address)
            except User.DoesNotExist:
                 return Response({'message': 'No user with this email exists.'}, status=status.HTTP_404_NOT_FOUND)

            # Generate or retrieve a password reset token
            token, created = PasswordResetToken.objects.get_or_create(user=user)
            if not created:
                token.token = uuid.uuid4()
                token.created_at = datetime.now()
                token.save()

            # Construct the correct reset link
            reset_link = f"http://127.0.0.1:8000/password-reset/{token.token}/"

            # Send email notification
            subject = "Password Reset Request"
            message = f"Click the link below to reset your password:\n\n{reset_link}"
            send_mail(
            subject='Password Reset',
            message='Your reset link is...',
            from_email='pierre@nguweneza.tech"',  # Ensure this is valid
            recipient_list='charlotteliz22@gmail.com',
            fail_silently=False,
          )


            return Response({'message': 'Password reset email sent.'}, status=status.HTTP_200_OK)

        # Debugging print statement for errors
        print(serializer.errors)  # Debugging line
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetAPIView(APIView):
    def post(self, request, token):
        try:
            reset_token = PasswordResetToken.objects.get(token=token)
        except PasswordResetToken.DoesNotExist:
            return Response({'message': 'Invalid token.'}, status=status.HTTP_400_BAD_REQUEST)

        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if not new_password:
            return Response({'message': 'New password is required.'}, status=status.HTTP_400_BAD_REQUEST)

        if new_password != confirm_password:
            return Response({'message': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

        if len(new_password) < 8:
            return Response({'message': 'Ensure this field has at least 8 characters.'}, status=status.HTTP_400_BAD_REQUEST)

        user = reset_token.user
        user.set_password(new_password)
        user.save()

        # Delete the token after use
        reset_token.delete()

        return Response({'message': 'Password has been reset.'}, status=status.HTTP_200_OK)
