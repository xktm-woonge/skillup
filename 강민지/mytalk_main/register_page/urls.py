from django.urls import path
from . import views

app_name = 'register_page'

urlpatterns = [
    path('', views.load_register, name='register'),
    path('sendEmail_api/', views.get_email, name='email_api'),
    path('confirmCertNum_api/', views.conf_ceri_num, name='cert_conf_api'),
    path('confirmEmail_api/', views.conf_email, name='email_conf_api'),
    path('addUser_api/', views.add_user, name='add_user_api'),
]
