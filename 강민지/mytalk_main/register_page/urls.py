from django.urls import path
from . import views

app_name = 'register_page'

urlpatterns = [
    path('', views.load_register, name='register'),
    path('send-email/', views.get_email, name='email_api'),
    path('confirm-cert-num/', views.conf_ceri_num, name='cert_conf_api'),
    path('confirm-email/', views.conf_email, name='email_conf_api'),
    path('add-user/', views.add_user, name='add_user_api'),
]
