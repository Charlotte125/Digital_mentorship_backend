from rest_framework import serializers
from .models import Registration

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