from django.urls import path, include
from . import views

app_name = 'chatting_main_page'

urlpatterns = [
    path('', views.load_chattion_main_page, name='chat_home'),
    path('logout_api/', views.user_logout, name='logout_api'),
    path('push_data_api/', views.push_load_data, name='push_data_api'),
    path('get_message_api/', views.get_message_data, name='get_message_api'),
    path('send_message_api/', views.sended_message_data, name='send_message_api'),
    path('recive_chatbot_conv_api/', views.chatbot_conv, name='recive_chatbot_conv_api'),
]
