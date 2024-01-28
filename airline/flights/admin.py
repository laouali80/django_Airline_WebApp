from django.contrib import admin

from .models import Flight, Airport, Passenger
# Register your models here.

# configuration of admin for getting more information
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

# Special way of managing many to many relationship
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)
    
admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
