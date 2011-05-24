from django.conf.urls.defaults import *

urlpatterns = patterns('subscriptions.views',
    (r'^$', 'index'),
    (r'^add/$', 'add'),
)