from django.urls import path, include
from . import views

app_name = 'chatting_main_page'

urlpatterns = [
    path('', views.load_chatting_main_page, name='chat_home'),
    path('logout_api/', views.user_logout, name='logout_api'),
    path('push_data_api/', views.push_load_data, name='push_data_api'),
    path('get_message_api/', views.get_message_data, name='get_message_api'),
    path('set_changed_user_info_api/', views.set_changed_user_info, name='set_changed_user_info_api'),
    path('friend_request_api/', views.friend_request, name='friend_request_api'),
]