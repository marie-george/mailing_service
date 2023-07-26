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


class Contact(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    email = models.CharField(max_length=150, verbose_name='почта')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
        ordering = ('first_name',)


class Mailing_log(models.Model):
    time = models.DateTimeField(verbose_name='дата и время')
    attempt = models.BooleanField(default=True, verbose_name='статус попытки')
    server_response = models.BooleanField(default=True, verbose_name='ответ сервера')

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('server_response',)


class Mailing(models.Model):
    # message = models.ManyToManyField(Message, verbose_name='сообщение')
    # contact = models.ManyToManyField(Contact, verbose_name='контакт')
    # mailing_log = models.ManyToManyField(Mailing_log, verbose_name='логи рассылки')
    email = models.CharField(verbose_name='почта', **NULLABLE)
    header = models.CharField(verbose_name='тема', **NULLABLE)
    contents = models.TextField(verbose_name='содержание', **NULLABLE)
    time = models.TimeField(verbose_name='время рассылки')
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
    status = models.CharField(choices=statuses, verbose_name='статус рассылки')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('status',)

