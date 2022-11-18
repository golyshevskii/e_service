from django.shortcuts import render
from django.contrib import messages
from .tasks import send_mail_func

def main_page(request):
    return render(request, 'base.html')

def mail_send_page(request):
    send_mail_func.delay()
    messages.info(request, "Emails sent successfully!")
    return render(request, 'mailpage.html')
