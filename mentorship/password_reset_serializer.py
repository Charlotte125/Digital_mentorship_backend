from rest_framework import serializer




# class PasswordResetRequestSerializer(serializers.Serializer):  # Fixed indentation here
#     email = serializers.EmailField()

#     def validate_email(self, value):
#         if not User.objects.filter(email=value).exists():
#             raise serializers.ValidationError("No user with this email exists.")
#         return value
