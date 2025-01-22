from django.db import models
from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.timezone import now
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import AbstractUser





class User(AbstractUser):
    
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set', 
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    


class Registration(models.Model):
    student_id = models.CharField(max_length=1000, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    department = models.CharField(max_length=255)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class UniversityStaff(models.Model):
    staff_id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255, unique=True)
    department = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"


class Therapist(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    level_education = models.CharField(max_length=255, blank=False)
    email_address = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)   
    document = models.FileField(upload_to='documents/', blank=False, null=False)  

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Therapist, self).save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class PasswordResetToken(models.Model):
    
    email_address = models.EmailField(null=True, blank=True) 
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def generate_token(self):
        return str(uuid.uuid4())  
    
    def is_expired(self):
      
        return timezone.now() - self.created_at > timezone.timedelta(hours=1)


class Message(models.Model):
    first_name = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}: {self.message[:20]}..."        





