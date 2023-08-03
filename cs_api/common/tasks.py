from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_async(**args):
    send_mail(**args)
