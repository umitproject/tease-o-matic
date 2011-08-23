from django.conf.urls.defaults import *

urlpatterns = patterns('subscriptions.views',
    (r'^$', 'index'),
    (r'^subscription/add/$', 'add'),
)