from django.contrib import admin

from mailing.models import Mailing


@admin.register(Mailing)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'contents', 'time', 'interval', 'interval')
    search_fields = ('header', 'time')
    list_filter = ('time',)

