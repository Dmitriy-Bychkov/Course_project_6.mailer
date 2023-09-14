from django import forms

from mail.models import Mailing, Client, Message


class StyleFormMixin:
    """Класс-миксин для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "is_active":
                field.widget.attrs['class'] = 'form-control'


class MailingForm(StyleFormMixin, forms.ModelForm):
    """Класс для генерации формы создания рассылки"""

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner', None)
        super().__init__(*args, **kwargs)
        self.fields['clients'].queryset = self.fields['clients'].queryset.filter(owner=owner)
        self.fields['message'].queryset = self.fields['message'].queryset.filter(owner=owner)

    class Meta:
        model = Mailing
        exclude = ('owner',)


class ClientForm(StyleFormMixin, forms.ModelForm):
    """Класс для генерации формы создания клиентов-получателей рассылки"""

    class Meta:
        model = Client
        exclude = ('owner',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    """Класс для генерации формы рассылочного сообщения"""

    class Meta:
        model = Message
        exclude = ('owner',)
