from django.conf import settings
from django.core.mail import send_mail


def send_email(subject, message, recipient_list):
    '''
    Отправляет e-mail пользователю через втроенную функцию send_mail
    :param subject: заголовок сообщения
    :param message: текст сообщения
    :param recipient_list: список e-mail адресов получателей
    '''

    from_email = settings.EMAIL_HOST_USER

    try:
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    except:
        print('Ошибка отправки')
