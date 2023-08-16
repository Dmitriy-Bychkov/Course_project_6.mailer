from django.urls import path

from mail.apps import MailConfig
from mail.views import ClientListView

app_name = MailConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='list')
]
