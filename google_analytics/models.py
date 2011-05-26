from django.db import models
from django.conf import settings

#if getattr(settings, 'GOOGLE_ANALYTICS_MODEL', False):
class Analytics(models.Model):
    analytics_code = models.CharField(blank=True, max_length=100)

    def __unicode__(self):
        return u"%s" % (self.analytics_code)
