#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

from django.shortcuts import render_to_response, render_to_string, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from subscriptions.models import Subscription
from subscriptions.forms import SubscribeForm, UnsubscribeForm
from subscriptions.utils import send_mail

def index(request):
    if 'success' in request.GET and request.GET['success']=='1':
        success = True
    else:
        success = False
    form = SubscribeForm()
    return render_to_response('subscriptions/index.html', {
        'form': form, 'success': success,
    })

sender, to, cc='', bcc='', reply_to='', subject='', body='', html='', attachments=[], headers={}

def add(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # search if email was not registered yet
            if Subscription.objects.filter(email=email):

                return render_to_response('subscriptions/index.html', {
                    'form': form,
                    'error_message': 'Email already registered',
                })

            else:

                sub = Subscription()
                sub.email = email
                sub.originating_ip = request.META['REMOTE_ADDR']
                sub.save()
                
                # Send email confirming and providing user with links to unsubscribe.
                send_subscribe_email(sub.email)

                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('subscriptions.views.index') + '?success=1')

    else:
        form = SubscribeForm()
        
    return render_to_response('subscriptions/index.html', {
        'form': form,
    })

def remove(request):
    if request.method == 'GET':
        form = UnsubscribeForm(request.GET)
        if form.is_valid():
            email = form.cleaned_data['email']
            id = form.cleaned_data['id']

            # search if email is registered
            subscription = Subscription.objects.filter(email=email, pk=id)
            if subscription:
                # This means user is registered. Let's unsubscribe him
                sub = subscription[0]
                sub.subscribed = False
                sub.save()
                
                return render_to_response('subscriptions/unsubscribed.html')
            else:
                # Doesn't exist... someone is trying to cheat on us. Let's pretend all is good in zion
                return render_to_response('subscriptions/unsubscribed.html')
    
    return index(request)