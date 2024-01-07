from celery import shared_task
from twilio.rest import Client
from django.conf import settings

client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)


@shared_task
def send_sms(receiver, message):
    message = client.messages \
        .create(
        body=message,
        from_=settings.TWILIO_NUMBER,
        to=receiver
    )
    return message.sid
