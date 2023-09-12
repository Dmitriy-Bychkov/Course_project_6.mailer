from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogListView(ListView):
    """Контроллер блога для просмотра списка статей"""

    model = Blog


class BlogDetailView(DetailView):
    """Контроллер блога для детального просмотра статьи"""

    model = Blog

    def get_object(self, queryset=None):
        """Создаем счетчик просмотров"""

        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        return self.object
