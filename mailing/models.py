from django.utils import timezone

from django.db import models


from config import settings

NULLABLE = {'null': True, 'blank': True}


class Message(models.Model):
    header = models.CharField(max_length=150, verbose_name='тема')
    contents = models.TextField(verbose_name='содержание')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('header',)

    def __str__(self):
        return self.header


class Contact(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    email = models.CharField(max_length=150, verbose_name='почта')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('first_name',)

    def __str__(self):
        return self.email


class Mailing_log(models.Model):
    time = models.DateTimeField(verbose_name='дата и время')
    attempt = models.BooleanField(default=True, verbose_name='статус попытки')
    server_response = models.BooleanField(default=True, verbose_name='ответ сервера')
    # mailing = models.ForeignKey('Mailing', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('server_response',)


class Mailing(models.Model):
    message = models.ForeignKey(Message, verbose_name='сообщение', on_delete=models.PROTECT)
    contacts = models.ManyToManyField(Contact, verbose_name='контакты')
    # mailing_log = models.ManyToManyField(Mailing_log, verbose_name='логи рассылки')
    # email = models.CharField(verbose_name='почта', **NULLABLE)
    # header = models.CharField(verbose_name='тема', **NULLABLE)
    # contents = models.TextField(verbose_name='содержание', **NULLABLE)
    time = models.TimeField(verbose_name='время рассылки')
    # last_sent = models.TimeField(verbose_name='время последней отправки', default=None, **NULLABLE)
    last_sent = models.DateTimeField(verbose_name='время последней отправки', default=None, **NULLABLE)
    # stop_time = models.DateTimeField(verbose_name='время окончания рассылки', default=None, **NULLABLE)
    finish_time = models.DateTimeField(verbose_name='время окончания рассылки', default=None, **NULLABLE)
    start_time = models.DateTimeField(verbose_name='время начала рассылки', default=None, **NULLABLE)
    intervals = (
        ('раз/день', 'раз/день'),
        ('раз/неделя', 'раз/неделя'),
        ('раз/месяц', 'раз/месяц'),
    )
    interval = models.CharField(choices=intervals, verbose_name='периодичность')
    statuses = (
        ('завершена', 'завершена'),
        ('создана', 'создана'),
        ('запущена', 'запущена'),
    )
    status = models.CharField(choices=statuses, default='создана', verbose_name='статус рассылки')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('status',)

