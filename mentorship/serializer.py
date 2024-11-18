from rest_framework import serializers
from .models import Registration
from .models import Therapist
from .models import ResetPassword

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['student_id', 'first_name', 'last_name', 'email_address', 'department', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  
        }

class RegistrationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['student_id', 'first_name', 'last_name', 'email_address', 'department']



 
class TherapistRegistartionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Therapist
        fields = ['first_name', 'last_name', 'email_address', 'level_education', 'password', 'document'] 
        extra_kwargs = {
            'password': {'write_only': True}  
        } 



class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResetPassword
        fields = ['New_password', 'confirm_password'] 
        extra_kwargs = {
            'password': {'write_only': True}  
        }            