from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/main/(?P<user_id>\w+)/$", consumers.MainPageConsumer.as_asgi()),
    re_path(r'ws/main/(?P<user_id>\d+)/(?P<room_num>\d+)/$', consumers.ChatRoomConsumer.as_asgi()),
]