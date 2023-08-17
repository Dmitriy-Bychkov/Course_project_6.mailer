from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from mail.models import Client, Message


class IndexView(TemplateView):
    """Класс отображения главной страницы сервиса"""

    template_name = 'mail/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'

        return context


class ClientListView(ListView):
    """Контроллер для клиента"""

    model = Client


class MessageCreateView(CreateView):
    """Контроллер для создания нового сообщения"""

    model = Message
    fields = ('message_subject', 'message_text')
    success_url = reverse_lazy('mail:message_list')


class MessageListView(ListView):
    """Контроллер для просмотра списка сообщений"""

    model = Message


class MessageDetailView(DetailView):
    """Контроллер для детального просмотра сообщений"""

    model = Message


class MessageUpdateView(UpdateView):
    """Контроллер для редактирования сообщения"""

    model = Message
    fields = ('message_subject', 'message_text')

    def get_success_url(self):
        """
        Переопределение url-адреса для перенаправления
        после успешного редактирования
        """

        return reverse('message:view', args=[self.object.pk])


class MessageDelete(DeleteView):
    """Контроллер для удаления сообщения"""

    model = Message
    success_url = reverse_lazy('mail:message_list')
