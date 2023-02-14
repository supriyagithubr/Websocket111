import os
#import channels
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
import app.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
        app.routing.websocket_urlpatterns
    )

})

