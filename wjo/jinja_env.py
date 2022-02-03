from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment
from django.conf import settings
from django.utils.safestring import mark_safe
from django.templatetags.static import static
from django.contrib.humanize.templatetags.humanize import intcomma
from datetime import datetime
from django.utils import timezone
import re

# from shop.models import Category

def date_format(date_obj):
    return date_obj.strftime('%b %d, %Y')

def time_format(time_obj):
    return time_obj.strftime("%I:%M:%S %p")

def localtime(time):
    return timezone.localtime(time).strftime("%b %d, %Y %I:%M %p")

def environment(**options):
    env = Environment(**options)
    
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'MEDIA_URL': settings.MEDIA_URL,
        'now':datetime.now(),
        'date_format':date_format,
        'intcomma': intcomma,
        'time_format':time_format,
        'localtime': localtime,
        'DEBUG':settings.DEBUG,
        'BASE_URL':settings.BASE_URL,
    })
    return env
