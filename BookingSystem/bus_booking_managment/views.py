from django.shortcuts import render

from django.http import JsonResponse
from .models import city, Trip, Bus, Seat, Booking
from rest_framework import generics
from rest_framework import serializers
from .models import Booking
from django.shortcuts import get_object_or_404




def get_seats(request):
    start_city_id = request.GET.get('start_city_id')
    end_city_id = request.GET.get('end_city_id')

    trips = Trip.objects.filter(start_city_id=start_city_id, end_city_id=end_city_id)

    seats = Seat.objects.filter(bus__trip__in=trips, is_available=True)

    available_seats = []
    for seat in seats:
        available_seats.append({
            'id': seat.id,
            'number': seat.number,
            'bus_number': seat.bus.number,
            'start_city': seat.bus.trip.start_city.name,
            'end_city': seat.bus.trip.end_city.name
        })

    return JsonResponse( available_seats)


def book(request):
    user_id = request.POST.get('user_id')
    trip_id = request.POST.get('trip_id')
    seat_id = request.POST.get('seat_id')

    
    seat = get_object_or_404(Seat, id=seat_id, is_available=True)

    
    if not seat.bus.available_seats:
        return JsonResponse({'error': 'The bus is full'})

    # Create a new booking
    booking = Booking.objects.create(user_id=user_id, seat=seat, trip=seat.bus.trip)
    seat.is_available = False
    seat.save()
    seat.bus.available_seats -= 1
    seat.bus.save()

    return JsonResponse({'success': True})


  