from django.contrib import admin
from .models import *
from .models import UniversityStaff

admin.site.register(Registration)
admin.site.register(Therapist)
admin.site.register( UniversityStaff)


# admin.site.register(ResetPassword)
# admin.site.register(Therapist)
