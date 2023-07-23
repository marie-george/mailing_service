from django.contrib import admin

from mailing.models import Mailing, Contact, Message, Mailing_log


@admin.register(Message)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'contents')
    search_fields = ('header',)
    list_filter = ('header',)


@admin.register(Mailing)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'header', 'contents', 'email', 'time', 'interval', 'status', 'owner')
    search_fields = ('header', 'time')
    list_filter = ('time',)


@admin.register(Contact)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email')
    search_fields = ('last_name', 'email')
    list_filter = ('email',)


@admin.register(Mailing_log)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'attempt', 'server_response')
    search_fields = ('time',)
    list_filter = ('time',)


