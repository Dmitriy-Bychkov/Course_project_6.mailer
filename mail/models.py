from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    """Модель для клиента сервиса рассылок"""

    client_name = models.CharField(max_length=30, verbose_name='имя')
    client_email = models.EmailField(max_length=100, verbose_name='email')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.client_name}, {self.client_email}'

    class Meta:
        """Представление написания заголовков для клиента в админке"""

        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Message(models.Model):
    """Модель рассылочного сообщения"""

    message_subject = models.CharField(max_length=180, verbose_name='тема письма')
    message_text = models.TextField(verbose_name='cообщение')

    def __str__(self):
        return f'{self.message_subject}, {self.message_text}'

    class Meta:
        """Представление написания заголовков для письма в админке"""

        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"
