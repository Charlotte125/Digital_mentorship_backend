from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import PasswordResetRequestAPIView, PasswordResetAPIView
from .views import PasswordResetRequestAPIView, PasswordResetAPIView

from .views import RegistrationAPIView, RegistrationDetailAPIView, TherapistregistrationAPIView, RegistrationViewSet


router = DefaultRouter()
router.register(r'registrations', RegistrationViewSet) 

urlpatterns = [
    path('api/', include(router.urls)), 
    path('api/register/', RegistrationAPIView.as_view(), name='api_register'),  
    path('api/register/therapist/', TherapistregistrationAPIView.as_view(), name='api_register_therapist'),  
    path('api/registrations/<int:student_id>/', RegistrationDetailAPIView.as_view(), name='registration-detail'),
     path('password-reset/', PasswordResetRequestAPIView.as_view(), name='password-reset-request'),
    path('password-reset/<str:token>/', PasswordResetAPIView.as_view(), name='password-reset'),

    # path('password-reset/<uuid:token>/', PasswordResetAPIView.as_view(), name='password-reset'),
]
