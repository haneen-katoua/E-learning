"""
ASGI config for eLearning project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from newapp.routing import websocket_urlpatterns
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eLearning.settings')
django.setup()
django_asgi_app  = get_asgi_application()
from newapp.customMiddleware import TokenAuthMiddleware

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket":
            AllowedHostsOriginValidator(
                TokenAuthMiddleware(
                URLRouter(
                    websocket_urlpatterns
                )
                )
        ),
})



