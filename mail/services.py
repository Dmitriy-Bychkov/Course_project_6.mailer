from blog.models import Blog
from mail.models import Mailing
from django.conf import settings
from django.core.cache import cache


def send_mailing_task():
    """ Вызывает отправку рассылок """

    # выбрать все подходящие рассылки
    mailing_list = Mailing.get_objects_for_send()
    # запустить цикл по этим рассылкам
    for mailing in mailing_list:
        # вызвать метод send
        mailing.send()


def get_blog_cache():
    """ Настройка низкоуровневого кеширования для списка статей блога """

    if settings.CACHE_ENABLED:
        cache_key = 'blog_list'
        blog_list = cache.get(cache_key)
        if blog_list is None:
            category_list = Blog.objects.all()
            cache.set(cache_key, category_list, 60)
    else:
        blog_list = Blog.objects.all()
    return blog_list
