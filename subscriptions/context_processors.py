#!/usr/bin/env python
##
## Author: Adriano Monteiro Marques <adriano@umitproject.org>
##
## Copyright (C) 2011 S2S Network Consultoria e Tecnologia da Informacao LTDA
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU Affero General Public License as
## published by the Free Software Foundation, either version 3 of the
## License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Affero General Public License for more details.
##
## You should have received a copy of the GNU Affero General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

import logging

from django.conf import settings
from subscription.models import SubscriptionEmail

def config(request):
    subscription_email = SubscriptionEmail.objects.all()
    if subscription_email:
        subscription_email = subscription_email[0]
    else:
        subscription_email = "Hey thanks for subscribing! We'll keep you posted!"
    
    return {'TEASE_SITE_URL': settings.TEASE_SITE_URL,
            'SUBSCRIPTION_MESSAGE': subscription_email.message }