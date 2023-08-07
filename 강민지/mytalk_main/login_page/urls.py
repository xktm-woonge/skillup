from django.urls import path, include
from . import views

app_name = 'login_page'

urlpatterns = [
    path('', views.login_page_view, name='login'),
    path('register/', include('register_page.urls', namespace='register_page')),
    path('main/', include('chatting_main_page.urls', namespace='chatting_main_page')),
    path('login_api/', views.try_login, name='try_log_api')
]
