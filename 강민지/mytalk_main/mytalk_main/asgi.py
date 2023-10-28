import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytalk_main.settings")	# mysite 는 django 프로젝트 이름
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.

import chatting_main_page.routing

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                chatting_main_page.routing.websocket_urlpatterns	# chat 은 routing.py 가 들어있는 앱 이름
            )
        )
    ),
})