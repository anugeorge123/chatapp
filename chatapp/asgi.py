import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatapp.settings")
from channels.routing import get_default_application
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()

django.setup()
application = get_default_application()







