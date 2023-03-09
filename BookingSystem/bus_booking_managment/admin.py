from django.contrib import admin
from .models import Bus, Seat, Booking



@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('number_plate', 'capacity')

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'bus', 'is_available')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'seat', 'trip')


