from django.contrib import admin
from .models import *
from .models import UniversityStaff

admin.site.register(Registration)
admin.site.register(Therapist)
admin.site.register( UniversityStaff)


# admin.site.register(ResetPassword)
# admin.site.register(Therapist)

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ("user1", "user2","created_at")

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("room", "sender","content","timestamp")