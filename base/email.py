from config.settings import settings
from django.core.mail import send_mail


def send_email(subject, body):
    success = True
    try:
        send_mail(subject=subject,
                  message=subject,
                  html_message=body,
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[settings.DEFAULT_TO_EMAIL],
                  fail_silently=False
                  )
    except Exception as e:
        print(f"Error: El email no pudo ser enviado!!")
        success = False

    return success
