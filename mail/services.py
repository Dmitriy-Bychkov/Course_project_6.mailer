from django.conf import settings
from django.core.mail import send_mail

from mail.models import Mailing


def send_mail_task(subject, message, recipient_list):
    '''
    Отправляет e-mail пользователю через втроенную функцию send_mail
    :param subject: заголовок сообщения
    :param message: текст сообщения
    :param recipient_list: список e-mail адресов получателей
    '''

    from_email = settings.EMAIL_HOST_USER

    try:
        return send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    except Exception as e:
        print(f'Ошибка отправки {e}')
        raise


def send_mailing_task():
    """ Вызывает отправку рассылок """

    # выбрать все подходящие рассылки
    mailing_list = Mailing.get_objects_for_send()
    # запустить цикл по этим рассылкам
    for mailing in mailing_list:
        # вызвать метод send
        mailing.send()
