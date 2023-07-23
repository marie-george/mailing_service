from celery import shared_task

from config.celery import app
from mailing.service import send


@app.task
def send_email(header, contents, email):
    send(header, contents, email)

# @app.task
# def send_email(header, contents, email):
#     for contact in Contacts.objects.all():
#       send(header, contents, email)
