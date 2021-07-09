from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import onlineLudo.routing

application = ProtocolTypeRouter({
  "websocket": AuthMiddlewareStack(
        URLRouter(
            onlineLudo.routing.websocket_urlpatterns
        )
    ),
})