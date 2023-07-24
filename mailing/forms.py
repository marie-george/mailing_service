from django import forms

from mailing.models import Mailing, Contact


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        exclude = ('owner',)


class ContactForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('owner',)
