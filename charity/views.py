from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import loader

from charity.models import Charity, Donation
from charity.models import Event
def charity(request):
    allcharity = Charity.objects.all().values()

    template = loader.get_template('list.html')
    context = {
    'allcharity': allcharity,
  }
    return HttpResponse(template.render(context, request))

def details(request, id):
  ev = Event.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'event': ev,
  }
  return HttpResponse(template.render(context, request))

def events(request):
    charity_id = request.GET.get('charity_id', None)

    if charity_id:
        events = Event.objects.filter(charity_id=charity_id)
    else:
        events = Event.objects.all()

    all_charities = Charity.objects.all().values('id', 'name')
    template = loader.get_template('events.html')
    context = {
        'ev': events,
        'all_charities': all_charities,
    }
    return HttpResponse(template.render(context, request))
def handle_donate(request):
    if request.method == 'POST':
            # Retrieve data from the form
            donor_name = request.POST.get('donor_name')
            donor_email = request.POST.get('donor_email')
            donor_phone = request.POST.get('donor_phone')
            pay_method = request.POST.get('pay_method')
            trx_id = request.POST.get('trx_id')
            amount = request.POST.get('amount')
            donor_address = request.POST.get('donor_address')
            event_id = request.POST.get('event_id')
            donation = Donation.objects.create(
                donor_name=donor_name,
                donor_email=donor_email,
                donor_phone=donor_phone,
                pay_method=pay_method,
                trx_id=trx_id,
                amount=amount,
                donor_address=donor_address,
                event = Event.objects.get(id=event_id),
                charity = Event.objects.get(id=event_id).charity,
                date = datetime.now()
            )
            donation.save()
            return HttpResponse('Donation successful!')

def donate(request, id):
  ev = Event.objects.get(id=id)
  print(str(ev))
  template = loader.get_template('donate.html')
  context = {
    'event': ev,
  }
  return HttpResponse(template.render(context, request))


