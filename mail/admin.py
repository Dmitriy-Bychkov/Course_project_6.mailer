from django.contrib import admin

from mail.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """Представление раздела - "Клиенты" в админке"""

    list_display = ('id', 'client_name', 'client_email')
    search_fields = ('client_name', 'client_email',)
