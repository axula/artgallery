from django.conf import settings
from settings.models import Setting

def settings(request):
    return { 'settings' : Setting.objects.first(), }