from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from celery import shared_task
from core import settings

@shared_task(bind=True)
def send_mail_func(self):
    """Function that sending emails for all users"""
    users = get_user_model().objects.all()

    for user in users:
        context = {'username': user.username}

        mail_subject = "Cool Message For " + context['username']
        html_message = render_to_string('mail.html', context=context)
        plain_message = strip_tags(html_message)
        to_email = user.email

        send_mail(
            subject= mail_subject,
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )

    return "Emails sent"