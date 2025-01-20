from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.auth import  PasswordResetAPIView
from .views.auth import PasswordResetRequestAPIView
from .views.auth import send_reset_email, reset_password
from django.urls import path
from .views.auth import UniversityStaffCreateAPIView
from .views.auth import RegistrationAPIView, RegistrationDetailAPIView, TherapistregistrationAPIView, RegistrationViewSet , UniversityStaffLoginView , MessageView 
from .views.auth import LoginView
from .views.auth import get_user_count
from .views.chat import SendMessageView, CreateRoomView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'registrations', RegistrationViewSet) 

urlpatterns = [
    path('send-reset-email/', send_reset_email, name='send_reset_email'),
    path('reset-password/<uuid:token>/', reset_password, name='reset_password'),
    path('api/', include(router.urls)), 
    path('api/register/', RegistrationAPIView.as_view(), name='api_register'),  
    path('api/register/therapist/', TherapistregistrationAPIView.as_view(), name='api_register_therapist'),  
    path('api/registrations/<int:student_id>/', RegistrationDetailAPIView.as_view(), name='registration-detail'),
    path('password-reset/', PasswordResetRequestAPIView.as_view(), name='password-reset'),
    path('api/university-staff/', UniversityStaffCreateAPIView.as_view(), name='university_staff_create'),
    path('api/university-staff-login/', UniversityStaffLoginView.as_view(), name='university-staff-login'),
    path('api/messages/', MessageView.as_view(), name='messages_api'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/userCount', get_user_count, name='user-count'),


   
    path('api/university-staff/', UniversityStaffCreateAPIView.as_view(), name='university_staff_create'),
   

    #Authentication
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #chat url

    path('api/send-message/', SendMessageView.as_view(), name='send_message'),
    path('api/create-room/', CreateRoomView.as_view(), name='create_room'),

   
]
