from django.forms import ModelForm, TextInput, EmailInput,Textarea, NumberInput,RadioSelect 
from .models import Registration
from .models import ResetPassword
from .models import Therapist
from django.forms import TextInput
from django import forms



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['student_id', 'first_name', 'last_name', 'email_address', 'department', 'password']  # Use a list
        widgets = {
            'password': forms.PasswordInput(),  # To render password as a password field
        }

widgets = {
          'first_name':TextInput(attrs={'placeholder':'first_name'}),
           'email_address':EmailInput(attrs={'placeholder':'Email address'}),
           'department':TextInput(attrs={'placeholder':'department'}),
            '   password':TextInput(attrs={'placeholder':'   password'}),
           '  student_id ':Textarea(attrs={'placeholder':'  student_id '})
         }





# # class  ResetPasswordForm(ModelForm):
#     class Meta:
#         model=  ResetPassword
#         fields= {'New_password','confirm_password'}
#         widgets = {
          
#            'New_password':TextInput(attrs={'placeholder':'new password'}),
#            'confrim_password' : TextInput(attrs={'placeholder': 'confirm passowrd'}),}
        



        

# class TherapistForm(ModelForm):
#     class Meta:
#         model= Therapist
#         fields= {' first_name ','last_name ','level_education ', ' email_address','password',' document'}
#         widgets = {
#             'email_address': TextInput (attrs={'placeholder':'email address '}),
#             'password': NumberInput (attrs={'placeholder':'password'}),
#             ' document': TextInput (attrs={'placeholder':'document'}),
#              ' level_education ': TextInput (attrs={'placeholder':'level of education'}),
#                 ' last_name  ': TextInput (attrs={'placeholder':'first name'}),
#                    'first_name ': TextInput (attrs={'placeholder':'last name'}),




            
#         }







        
                