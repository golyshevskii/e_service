from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .tasks import send_mail_func
from .forms import SignUpForm

def main_page(request):
    return render(request, 'base.html')

def mail_send_page(request):
    send_mail_func.delay()
    messages.info(request, "Emails sent successfully!")
    return render(request, 'mailpage.html')

def signup_page(request):
    context = {'val_err': None, 'pass_err': None, 'form': None}

    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        try:
            validate_email(email)
        except ValidationError:
            context['val_err'] = 'Email Address is not valid'

        if password1 and password2 and password1 != password2:
            form = SignUpForm()
            context['pass_err'] = "Passwords don't match"
        elif not password1 or not password2:
            form = SignUpForm()
            context['pass_err'] = "Passwords are empty"
        else:
            form = SignUpForm(request.POST)

            if form.is_valid():
                form.save()
                messages.info(request, "Sign up successfully!")
                return redirect('mainpage')

        context['form'] = form

    return render(request, 'signup.html', context=context)
