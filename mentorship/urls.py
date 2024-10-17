from django.urls import path
from .views import RegistrationAPIView, RegistrationDetailAPIView  # Import the renamed views

urlpatterns = [
    path('api/register/', RegistrationAPIView.as_view(), name='api_register'),
    path('registration/<str:student_id>/', RegistrationDetailAPIView.as_view(), name='registration_detail'),
]
