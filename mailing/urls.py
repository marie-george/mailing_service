from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import HomeView, MailingCreateView, MailingUpdateView, MailingDeleteView, MailingDetailView, MailingListView

app_name = MailingConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('mailing/create/', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/update/<pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/delete/<pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailing_detail/<pk>/', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing_list/', MailingListView.as_view(), name='mailing_list'),
]