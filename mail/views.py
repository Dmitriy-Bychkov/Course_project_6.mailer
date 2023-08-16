from django.views.generic import ListView

from mail.models import Client


class ClientListView(ListView):
    """Контроллер для с клиентом"""

    model = Client
