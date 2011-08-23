from django.conf.urls.defaults import *

handler500 = 'djangotoolbox.errorviews.server_error'

# for admin
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    (r'', include('subscriptions.urls')),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^admin/', include(admin.site.urls)),
    #(r'^page/$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    #('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
)
