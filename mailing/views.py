from django.shortcuts import render
from django.views import generic
from django.urls import reverse, reverse_lazy

from mailing.models import Mailing
from mailing.forms import MailingForm


class HomeView(generic.TemplateView):
    template_name = 'mailing/home.html'
    extra_context = {
        'title': 'Главная страница',
        # 'object_list': Blog.objects.all()[:4],
    }

class MailingCreateView(generic.CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:home')

    # def form_valid(self, form):
    #     self.object = form.save()
    #     self.object.owner = self.request.user
    #     self.object.save()
    #
    #     return super().form_valid(form)