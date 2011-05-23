from django.conf.urls.defaults import *
from minicms.models import PagesSitemap

handler500 = 'djangotoolbox.errorviews.server_error'

# for admin
from django.contrib import admin
admin.autodiscover()

sitemaps = {
    'pages': PagesSitemap,
}

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    (r'^admin/', include(admin.site.urls)),
    #(r'^page/$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    #('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
)
