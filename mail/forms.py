from django import forms

from mail.models import Mailing


class StyleFormMixin:
    """Класс-миксин для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):
    """Класс для генерации формы создания рассылки"""

    class Meta:
        model = Mailing
        fields = "__all__"
