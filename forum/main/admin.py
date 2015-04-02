from django.contrib import admin

from main.models import Message

class MessageAdmin(admin.ModelAdmin):
    model = Message

admin.site.register(Message, MessageAdmin)
