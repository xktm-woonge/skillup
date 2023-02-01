from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.chatbotView, name='chathome'),
    path('chatting/', views.sendChatBody, name='chatting'),
]
