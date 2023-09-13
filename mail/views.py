from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
import random
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from blog.models import Blog
from mail.forms import MailingForm, ClientForm, MessageForm
from mail.models import Client, Message, Mailing, Log


class IndexView(TemplateView):
    """Класс отображения главной страницы сервиса"""

    template_name = 'mail/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'

        # Получение количества рассылок всего
        total_mailings = Mailing.objects.count()
        context['total_mailings'] = total_mailings

        # Получение количества активных рассылок
        active_mailings = Mailing.objects.filter(is_active=True).count()
        context['active_mailings'] = active_mailings

        # Получение количества уникальных клиентов для рассылок
        unique_clients = Client.objects.count()
        context['unique_clients'] = unique_clients

        # Получение всех статей блога
        all_blogs = list(Blog.objects.all())

        if len(all_blogs) >= 3:
            # Получение трёх случайных статей из блога
            random_blogs = random.sample(all_blogs, 3)
        else:
            # Если количество статей меньше 3, выводим все статьи
            random_blogs = all_blogs

        context['random_blogs'] = random_blogs

        return context


class ClientCreateView(CreateView):
    """Контроллер для создания нового клиента - получателя рассылки"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')


class ClientListView(ListView):
    """Контроллер для просмотра списка клиентов"""

    model = Client


class ClientDetailView(DetailView):
    """Контроллер для детального просмотра клиента"""

    model = Client


class ClientUpdateView(UpdateView):
    """Контроллер для редактирования клиента"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:clients_list')


class ClientDelete(DeleteView):
    """Контроллер для удаления клиента"""

    model = Client
    success_url = reverse_lazy('mail:clients_list')


class MessageCreateView(CreateView):
    """Контроллер для создания нового сообщения"""

    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mail:messages_list')


class MessageListView(ListView):
    """Контроллер для просмотра списка сообщений"""

    model = Message


class MessageDetailView(DetailView):
    """Контроллер для детального просмотра сообщения"""

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
    """Контроллер для просмотра списка рассылок"""

    model = Mailing


class MailingDetailView(DetailView):
    """Контроллер для детального просмотра рассылки"""

    model = Mailing


class MailingUpdateView(UpdateView):
    """Контроллер для редактирования рассылки"""

    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail:mailing_list')


class MailingDelete(DeleteView):
    """Контроллер для удаления рассылки"""

    model = Mailing
    success_url = reverse_lazy('mail:mailing_list')


class LogListView(ListView):
    """Контроллер для просмотра списка логов рассылок"""

    model = Log
