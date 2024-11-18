from django.db import models
from django.contrib.auth.hashers import make_password
from django.db import models

class Registration(models.Model):
    student_id = models.CharField(max_length=1000, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    department = models.CharField(max_length=255)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Therapist(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    level_education = models.CharField(max_length=255, blank=False)
    email_address = models.EmailField(max_length=255, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)   
    document = models.FileField(upload_to='documents/', blank=False, null=False)  

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Therapist, self).save(*args, **kwargs)



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class ResetPassword(models.Model):
        New_password = models.CharField(max_length=128,blank=False,null=False)
        confirm_password = models.CharField(max_length=128,blank=False,null=False)
    









