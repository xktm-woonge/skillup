from django.urls import path

from . import consumers

websochet_urlpatterns = [
    path('main/<str:room_name>', consumers.ChatConsumer.as_asgi())
]