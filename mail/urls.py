from django.urls import path
from .views import mail_send_page, main_page, signup_page


urlpatterns = [
    path('', main_page, name='mainpage'),
    path('signup/', signup_page, name='signup'),
    path('mail/',mail_send_page, name='mailpage'),
]