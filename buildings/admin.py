from django.contrib import admin
from .models import Building, Floor, Room, Reservation
# Register your models here.
admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Reservation)
