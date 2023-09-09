from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from mail.forms import MailingForm, ClientForm, MessageForm
from mail.models import Client, Message, Mailing


class IndexView(TemplateView):
    """Класс отображения главной страницы сервиса"""

    template_name = 'mail/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'

        return context


class ClientCreateView(CreateView):
    """Контроллер для создания новой рассылки"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')


class ClientListView(ListView):
    """Контроллер для клиента"""

    model = Client


class MessageCreateView(CreateView):
    """Контроллер для создания нового сообщения"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail:messages_list')


class MessageListView(ListView):
    """Контроллер для просмотра списка сообщений"""

    model = Message


class MessageDetailView(DetailView):
    """Контроллер для детального просмотра сообщений"""

    model = Message


class MessageUpdateView(UpdateView):
    """Контроллер для редактирования сообщения"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail:messages_list')


class MessageDelete(DeleteView):
    """Контроллер для удаления сообщения"""

    model = Message
    success_url = reverse_lazy('mail:messages_list')


class MailingCreateView(CreateView):
    """Контроллер для создания новой рассылки"""

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail:mailing_list')


class MailingListView(ListView):
    """Контроллер для списка рассылок"""

    model = Mailing
