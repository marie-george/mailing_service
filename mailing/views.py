from celery import Celery
from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy

from blog.models import Blog
from mailing.models import Mailing, Contact, Message
from mailing.forms import MailingForm, ContactForm, MessageForm
from mailing.service import send
# from mailing.tasks import send_email
from random import choices

app = Celery()

# Домашняя страница ========================================================================================
class HomeView(generic.TemplateView):
    template_name = 'mailing/home.html'
    extra_context = {
        'title': 'Главная страница',
        'object_list': choices(Blog.objects.all(), k=3),
        'mailing_count': Mailing.objects.count(),
        'active_mailing_count': Mailing.objects.filter(status='запущена').count(),
        'unique_client_count': len({contact.email for contact in Contact.objects.all()})
    }

# Рассылка ===============================================================================================
class MailingCreateView(generic.CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')


    # @app.on_after_configure.connect
    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        # send(form.instance.header, form.instance.contents, form.instance.email)
        # end_semail.delay(form.instance.header, form.instance.contents, form.instance.email)
        self.object.save()

        return super().form_valid(form)


class MailingUpdateView(generic.UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def form_valid(self, form):
        self.object = form.save()
        # send_email.delay(form.instance.header, form.instance.contents, form.instance.email)
        self.object.save()

        return super().form_valid(form)


class MailingDeleteView(generic.DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')


class MailingDetailView(generic.DetailView):
    model = Mailing


class MailingListView(generic.ListView):
    model = Mailing

# Контакты ==================================================================================================
class ContactListView(generic.ListView):
    model = Contact


class ContactDetailView(generic.DetailView):
    model = Contact


class ContactCreateView(generic.CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('mailing:contact_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ContactUpdateView(generic.UpdateView):
    model = Contact
    fields = ('first_name', 'last_name', 'email')
    success_url = reverse_lazy('mailing:contact_list')


class ContactDeleteView(generic.DeleteView):
    model = Contact
    success_url = reverse_lazy('mailing:contact_list')


# Сообщения ===============================================================================================
class MessageListView(generic.ListView):
    model = Message


class MessageDetailView(generic.DetailView):
    model = Message


class MessageCreateView(generic.CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')


class MessageUpdateView(generic.UpdateView):
    model = Message
    fields = ('header', 'contents')
    success_url = reverse_lazy('mailing:message_list')


class MessageDeleteView(generic.DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')
