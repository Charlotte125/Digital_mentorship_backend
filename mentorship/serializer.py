from rest_framework import serializers
from .models import Registration, Therapist, PasswordResetToken
from django.contrib.auth.models import User


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

class PasswordResetSerializer(serializers.Serializer):
    email_address = serializers.EmailField(required=True)
    new_password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

def validate_email(self, value):
    try:
        User.objects.get(email__iexact=value) 
        return value
    except User.DoesNotExist:
        raise serializers.ValidationError("No user with this email exists.")

    def validate(self, data):
        """Ensure the new_password and confirm_password match."""
        if data["new_password"] != data["confirm_password"]:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data


