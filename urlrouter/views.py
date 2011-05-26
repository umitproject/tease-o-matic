from .api import handlers
from .models import URLRoute
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

def show(request, url):
    if not url.endswith('/') and settings.APPEND_SLASH:
        return HttpResponseRedirect("%s/" % request.path)
    if not url.startswith('/'):
        url = "/" + url
    route = get_object_or_404(URLRoute, url=url)
    return handlers[route.handler].dispatch(request, route.target)
