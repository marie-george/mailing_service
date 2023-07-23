from django.db import models
from django.urls import reverse
from pytils.translit import slugify

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Message(models.Model):
    header = models.CharField(max_length=150, verbose_name='тема')
    contents = models.TextField(verbose_name='содержание')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('header',)


class Mailing(models.Model):
    header = models.CharField(max_length=150, verbose_name='тема')
    contents = models.TextField(verbose_name='содержание')
    email = models.CharField(max_length=150, verbose_name='почта', **NULLABLE)
    # message = models.ForeignKey(Message, on_delete = models.CASCADE)
    time = models.TimeField(verbose_name='время рассылки')
    intervals = (
        ('D', 'once/day'),
        ('W', 'once/week'),
        ('M', 'once/month'),
    )
    interval = models.CharField(choices=intervals, verbose_name='периодичность')
    # статус рассылки: завершена, создана, запущена
    statuses = (
        ('F', 'finished'),
        ('C', 'created'),
        ('I', 'initiated'),
    )
    status = models.CharField(choices=statuses, verbose_name='статус рассылки')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('status',)


class Mailing_log(models.Model):
    time = models.DateTimeField(verbose_name='дата и время')
    attempt = models.BooleanField(default=True, verbose_name='статус попытки')
    server_response = models.BooleanField(default=True, verbose_name='ответ сервера')

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('server_response',)


class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URl')
    contents = models.TextField(verbose_name='содержание')
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    published = models.DateField(verbose_name='дата публикации')
    views_number = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def increase_view_count(self):
        self.views_number += 1
        self.save()

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
        ordering = ('name',)
