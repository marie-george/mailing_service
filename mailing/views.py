from celery import Celery
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy

from blog.models import Blog
from mailing.models import Mailing, Contact, Message
from mailing.forms import MailingForm, ContactForm, MessageForm, MailingListForm, ContactListForm, MessageListForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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
class MailingCreateView(LoginRequiredMixin, generic.CreateView):
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


class MailingUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:mailing_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied()
        return self.object

    def form_valid(self, form):
        self.object = form.save()
        # send_email.delay(form.instance.header, form.instance.contents, form.instance.email)
        self.object.save()

        return super().form_valid(form)


class MailingDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailing:mailing_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied()
        return self.object


class MailingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Mailing

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied()
        return self.object


class MailingListView(LoginRequiredMixin, generic.ListView):
    model = Mailing
    form_class = MailingListForm
    template_name = 'mailing/mailing_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


# Контакты ==================================================================================================
class ContactListView(LoginRequiredMixin, generic.ListView):
    model = Contact
    form_class = ContactListForm
    template_name = 'mailing/contact_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class ContactDetailView(LoginRequiredMixin, generic.DetailView):
    model = Contact

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied()
        return self.object


class ContactCreateView(LoginRequiredMixin, generic.CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('mailing:contact_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Contact
    fields = ('first_name', 'last_name', 'email')
    success_url = reverse_lazy('mailing:contact_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied()
        return self.object


class ContactDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Contact
    success_url = reverse_lazy('mailing:contact_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied()
        return self.object


# Сообщения ===============================================================================================
class MessageListView(LoginRequiredMixin, generic.ListView):
    model = Message
    form_class = MessageListForm
    template_name = 'mailing/message_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class MessageDetailView(LoginRequiredMixin, generic.DetailView):
    model = Message

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied()
        return self.object


class MessageCreateView(LoginRequiredMixin, generic.CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailing:message_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Message
    fields = ('header', 'contents')
    success_url = reverse_lazy('mailing:message_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied()
        return self.object


class MessageDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Message
    success_url = reverse_lazy('mailing:message_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise PermissionDenied()
        return self.object
