from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  PasswordResetAPIView
from .views import PasswordResetRequestAPIView
from . import views
from django.urls import path
from .views import RegistrationAPIView, RegistrationDetailAPIView, TherapistregistrationAPIView, RegistrationViewSet


router = DefaultRouter()
router.register(r'registrations', RegistrationViewSet) 

urlpatterns = [
    path('send-reset-email/', views.send_reset_email, name='send_reset_email'),
    path('reset-password/<uuid:token>/', views.reset_password, name='reset_password'),
    path('api/', include(router.urls)), 
    path('api/register/', RegistrationAPIView.as_view(), name='api_register'),  
    path('api/register/therapist/', TherapistregistrationAPIView.as_view(), name='api_register_therapist'),  
    path('api/registrations/<int:student_id>/', RegistrationDetailAPIView.as_view(), name='registration-detail'),
    path('password-reset/', PasswordResetRequestAPIView.as_view(), name='password-reset'),
    # path('password-reset/<str:token>/', PasswordResetAPIView.as_view(), name='password-reset'),

   
]
