from subscriptions.models import Subscription
from subscriptions.forms import SubscribeForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    if 'success' in request.GET and request.GET['success']=='1':
        success = True
    else:
        success = False
    form = SubscribeForm()
    return render_to_response('subscriptions/index.html', {
        'form': form, 'success': success,
    })


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

                sub = Subscription(email=email)
                sub.save()

                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('subscriptions.views.index') + '?success=1')

    else:
        form = SubscribeForm()
        
    return render_to_response('subscriptions/index.html', {
        'form': form,
    })