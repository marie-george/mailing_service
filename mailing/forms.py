from django import forms

from mailing.models import Mailing, Contact, Message


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class MailingForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Mailing
        exclude = ('owner',)

    def __init__(self, user=None, **kwargs):
        super(MailingForm, self).__init__(**kwargs)
        if user:
            self.fields['contact'].queryset = Contact.objects.filter(user=user)


class ContactForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Contact
        exclude = ('owner',)

class MessageForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Message
        exclude = ('owner',)


class MailingListForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        exclude = ('owner',)


class ContactListForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class MessageListForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
