from django.db import models


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
    # message = models.ForeignKey(Message, on_delete = models.CASCADE)

    email = models.CharField(max_length=150, verbose_name='почта', **NULLABLE)
    # email = models.ForeignKey(Contact, on_delete = models.CASCADE)
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


class Contact(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    email = models.CharField(max_length=150, verbose_name='почта')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('first_name',)


