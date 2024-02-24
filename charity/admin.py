from django.contrib import admin

from .models import Charity, Event, Donation
admin.site.register(Charity)
admin.site.register(Event)
admin.site.register(Donation)
