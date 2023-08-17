from django.contrib import admin

from mail.models import Client, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Представление раздела - "Клиенты" в админке"""

    list_display = ('id', 'client_name', 'client_email')
    search_fields = ('client_name', 'client_email', 'comment',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Представление раздела - "Сообщения" в админке"""

    list_display = ('id', 'message_subject', 'message_text')
    search_fields = ('message_subject', 'message_text',)
