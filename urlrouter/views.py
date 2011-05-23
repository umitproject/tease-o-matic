from .api import handlers
from .models import URLRoute
from django.shortcuts import get_object_or_404

def show(request, url):
    print URLRoute.objects.all()
    route = get_object_or_404(URLRoute, url=url)
    return handlers[route.handler].dispatch(request, route.target)
