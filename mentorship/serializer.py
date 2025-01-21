from rest_framework import serializers
from .models import Registration, Therapist, PasswordResetToken 
from django.contrib.auth.models import User
from .models import UniversityStaff , Message
from rest_framework import serializers



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
    email_address = serializers.EmailField()
    new_password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if not User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("No user with this email exists.")
        return value

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data



class UniversityStaffSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = UniversityStaff
        fields = ['staff_id', 'first_name', 'last_name', 'email_address', 'department', 'role', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password') 
        staff = UniversityStaff(**validated_data)
        staff.set_password(validated_data['password'])  
        staff.save()
        return staff  




class StaffLoginSerializer(serializers.Serializer):
    email_address = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)   



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'first_name', 'message', 'timestamp']   



class LoginSerializer(serializers.Serializer):
    email_address = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email_address = data.get('email_address')
        password = data.get('password')

        try:
            therapist = Therapist.objects.get(email_address=email_address)
        except Therapist.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")

        if not therapist.check_password(password):
            raise serializers.ValidationError("Invalid email or password.")

        data['therapist'] = therapist
        return data           

