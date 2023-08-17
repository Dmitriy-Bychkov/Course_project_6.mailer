from django.urls import path

from mail.apps import MailConfig
from mail.views import ClientListView, MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, \
    MessageDelete, IndexView

app_name = MailConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('434/', ClientListView.as_view(), name='client_list'),
    path('create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/', MessageListView.as_view(), name='message_list'),
    path('view/<int:pk>/', MessageDetailView.as_view(), name='message_view'),
    path('edit/<int:pk>/', MessageUpdateView.as_view(), name='message_edit'),
    path('delete/<int:pk>/', MessageDelete.as_view(), name='message_delete'),
]
