from django.urls import path, include
from . import views

app_name = 'chatting_main_page'

urlpatterns = [
    path('', views.load_chattion_main_page, name='chat_home'),
]
