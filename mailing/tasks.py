from celery import shared_task

from config.celery import app
from mailing.service import send


@shared_task
def send_email(header, contents, email):
    send(header, contents, email)


