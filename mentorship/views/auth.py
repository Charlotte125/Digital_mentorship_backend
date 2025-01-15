from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from ..models import Registration
from ..serializer import RegistrationSerializer, RegistrationDetailSerializer  ,TherapistRegistartionSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from ..models import PasswordResetToken
from rest_framework.exceptions import ValidationError
from ..serializer import PasswordResetSerializer  
import uuid
from datetime import datetime
import smtplib
from django.conf import settings
import logging
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.core .mail import send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import PasswordChangeForm
from ..models import PasswordResetToken
from ..models import UniversityStaff
from ..serializer import UniversityStaffSerializer



def send_reset_email(request):
    """Handle password reset request, generate token and send email."""
    if request.method == 'POST':
        receiver_email = request.POST.get('email')

        try:
            
            user = Registration.objects.get(email_address=receiver_email)

         
            token = str(uuid.uuid4())
            PasswordResetToken.objects.create(email_address=receiver_email, token=token)

            reset_link = f'{settings.FRONTEND_URL}/reset-password/{token}/'

           
            context = {'reset_link': reset_link}
            message = render_to_string('index.html', context)

            send_mail(
                'Password Reset Request',
                '',  
                settings.EMAIL_HOST_USER,
                [receiver_email],
                fail_silently=False,
                html_message=message,
            )

            return JsonResponse({'success': True, 'message': 'Password reset email sent successfully!'})
        
        except Registration.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User not found.'})

    return HttpResponse({'success': False, 'message': 'Invalid request method. POST expected.'})


def reset_password(request, token):
    """Handle password reset using the token."""
    if request.method == 'POST':
        try:
            n
            reset_token = PasswordResetToken.objects.get(token=token)
            user = Registration.objects.get(email_address=reset_token.email_address)

         
            new_password = request.POST.get('new_password')

    
            user.set_password(new_password)
            user.save()

            reset_token.delete()

            return JsonResponse({'success': True, 'message': 'Password reset successful.'})
        
        except (PasswordResetToken.DoesNotExist, Registration.DoesNotExist):
            return JsonResponse({'success': False, 'message': 'Invalid token or user not found.'})

    return JsonResponse({'success': False, 'message': 'Invalid request method. POST expected.'})

class RegistrationAPIView(APIView):  
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
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)  
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
    queryset = Registration.objects.all()  
    serializer_class = RegistrationSerializer 


class PasswordResetRequestAPIView(APIView):
    def post(self, request):
        logger.info("Password reset request received.")
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email_address = serializer.validated_data.get('email_address')
            logger.info(f"Validated email: {email_address}")

            user = User.objects.filter(email__iexact=email_address).first()
            if not user:
            
                return Response(
                    {'message': 'No user with this email exists.'},
                    status=status.HTTP_404_NOT_FOUND
                )
        
            token, _ = PasswordResetToken.objects.get_or_create(user=user)
            reset_link = f"http://127.0.0.1:8000/password-reset/{token.token}/"
            logger.info(f"Generated reset link: {reset_link}")

            
            send_mail(
                subject="Password Reset",
                message=f"Click the link below to reset your password:\n\n{reset_link}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email_address],
                fail_silently=False,
            )

            return Response(
                {'message': 'Password reset email sent.'},
                status=status.HTTP_200_OK
            )

        logger.error("Serializer validation failed.")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def email_exists(self, email):
  """Check if the given email exists in the database."""
  return (
      User.objects.filter(email__iexact=email).exists() or
    #  user = User.objects.filter(email__iexact='raissa@gmail.com').first() print(user) or
    #  user = User.objects.filter(email__iexact='raissa@gmail.com').first()
    #  print(user) or
     Registration.objects.filter(email_address__iexact=email).exists()
  )

def send_test_email():
  try:
    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.starttls()
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    message = "This is a test email from your Django application."
    server.sendmail(settings.DEFAULT_FROM_EMAIL, ["pierre@nguweneza.tech"], message)
    server.quit()
    print("Email sent successfully!")
  except Exception as e:
    print(f"Error sending email: {e}")

if __name__ == "__main__":
  send_test_email()




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

    
        reset_token.delete()

        return Response({'message': 'Password has been reset.'}, status=status.HTTP_200_OK)



class UniversityStaffCreateAPIView(APIView):
    def post(self, request):
        serializer = UniversityStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "University staff registered successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       





