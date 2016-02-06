from django.contrib import admin

from backend.models import *

# Register your models here.

admin.site.register(UserData)
admin.site.register(Trip)
admin.site.register(Feedback)
admin.site.register(ChatMessage)