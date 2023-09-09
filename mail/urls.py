from django.urls import path

from mail.apps import MailConfig
from mail.views import ClientListView, MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, \
    MessageDelete, IndexView, MailingCreateView

app_name = MailConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('clients_list/', ClientListView.as_view(), name='clients_list'),
    path('create_message/', MessageCreateView.as_view(), name='create_message'),
    path('messages_list/', MessageListView.as_view(), name='messages_list'),
    path('view_message/<int:pk>/', MessageDetailView.as_view(), name='view_message'),
    path('edit_message/<int:pk>/', MessageUpdateView.as_view(), name='edit_message'),
    path('delete_message/<int:pk>/', MessageDelete.as_view(), name='delete_message'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
]
