from celery import shared_task
import time
from django.core.mail import send_mail
from celery.exceptions import MaxRetriesExceededError

@shared_task
def add(x, y):
    time.sleep(5)  # Simulate a time-consuming task
    return x + y


@shared_task
def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'noreply@myapp.com',
        recipient_list,
        fail_silently=False,
    )
    
@shared_task(bind=True, max_retries=3)
def unreliable_task(self):
    try:
        # Simulate a task that fails occasionally
        result = 1 / 0
    except Exception as exc:
        raise self.retry(exc=exc, countdown=10)