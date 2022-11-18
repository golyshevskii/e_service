from django.urls import path
from .views import mail_send_page, main_page


urlpatterns = [
    path('', main_page, name='mainpage'),
    path('mail/',mail_send_page, name='mailpage'),
]