from config.celery import app as celery_app
from .email import send_email


@celery_app.task
def send_email_task(subject: str, body: str):
    return send_email(subject=subject, body=body)

