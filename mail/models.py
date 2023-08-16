from django.db import models


class Client(models.Model):
    """Модель для клиента сервиса рассылок"""

    client_name = models.CharField(max_length=30, verbose_name='имя')
    client_email = models.EmailField(max_length=100, verbose_name='email')

    def __str__(self):
        return f'{self.client_name}, {self.client_email}'

    class Meta:
        """Представление написания заголовков в админке"""

        verbose_name = "клиент"
        verbose_name_plural = "клиенты"
