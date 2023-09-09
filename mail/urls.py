from django.urls import path

from mail.apps import MailConfig
from mail.views import ClientListView, MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, \
    MessageDelete, IndexView, MailingCreateView, ClientCreateView, MailingListView

app_name = MailConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clients/create_client/', ClientCreateView.as_view(), name='create_client'),
    path('clients/clients_list/', ClientListView.as_view(), name='clients_list'),
    path('messages/create_message/', MessageCreateView.as_view(), name='create_message'),
    path('messages/messages_list/', MessageListView.as_view(), name='messages_list'),
    path('messages/view_message/<int:pk>/', MessageDetailView.as_view(), name='view_message'),
    path('messages/edit_message/<int:pk>/', MessageUpdateView.as_view(), name='edit_message'),
    path('messages/delete_message/<int:pk>/', MessageDelete.as_view(), name='delete_message'),
    path('mailings/create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('mailings/mailing_list/', MailingListView.as_view(), name='mailing_list'),
]
