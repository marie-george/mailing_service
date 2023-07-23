# Generated by Django 4.2.3 on 2023-07-23 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='наименование')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URl')),
                ('contents', models.TextField(verbose_name='содержание')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение')),
                ('published', models.DateField(verbose_name='дата публикации')),
                ('views_number', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='время рассылки')),
                ('interval', models.CharField(choices=[('D', 'once/day'), ('W', 'once/week'), ('M', 'once/month')], verbose_name='периодичность')),
                ('status', models.CharField(choices=[('F', 'finished'), ('C', 'created'), ('I', 'initiated')], verbose_name='статус рассылки')),
            ],
            options={
                'verbose_name': 'рассылка',
                'verbose_name_plural': 'рассылки',
                'ordering': ('status',),
            },
        ),
        migrations.CreateModel(
            name='Mailing_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='дата и время')),
                ('attempt', models.BooleanField(default=True, verbose_name='статус попытки')),
                ('server_response', models.BooleanField(default=True, verbose_name='ответ сервера')),
            ],
            options={
                'verbose_name': 'лог',
                'verbose_name_plural': 'логи',
                'ordering': ('server_response',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=150, verbose_name='содержание')),
                ('contents', models.TextField(verbose_name='содержание')),
            ],
            options={
                'verbose_name': 'сообщение',
                'verbose_name_plural': 'сообщения',
                'ordering': ('header',),
            },
        ),
    ]
