from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import HomeView, MailingCreateView

app_name = MailingConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
]