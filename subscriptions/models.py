from django.db import models

class Subscription(models.Model):
    email = models.CharField(max_length=100)

    def __unicode__(self):
        return self.email