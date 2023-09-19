from django.core.management import BaseCommand
from mail.services import send_mailing_task


class Command(BaseCommand):
    """Класс для отправки сообщений Кроном"""

    def handle(self, *args, **options):
        send_mailing_task()
