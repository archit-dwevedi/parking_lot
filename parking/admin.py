from django.contrib import admin

from .models import ParkingSpace, Parking, Rate

admin.site.register(Parking)
admin.site.register(ParkingSpace)
admin.site.register(Rate)
