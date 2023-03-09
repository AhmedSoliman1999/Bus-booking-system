
from django.urls import reverse
from .models import city, Trip, Bus, Seat, Booking
from django.test import TestCase
from django.test import  Client


class FleetManagementSystemTest(TestCase):

    def setUp(self):
        self.client = Client()

       
        self.cairo = city.objects.create(name='cairo')
        self.giza = city.objects.create(name='giza')
        self.alfayyum = city.objects.create(name='fayuum')
        self.alminya = city.objects.create(name='Minya')
        self.asyut = city.objects.create(name='Asyut')

        
        self.trip1 = Trip.objects.create(start_city=self.cairo, end_city=self.asyut)
        self.trip1.in_between_cities.add(self.alfayyum, self.alminya)

        
        self.bus1 = Bus.objects.create(number='ABC123', trip=self.trip1, available_seats=12)
        self.seat1 = Seat.objects.create(number=1, bus=self.bus1, is_available=True)
        

        
        self.booking1 = Booking.objects.create(user_id=1, seat=self.seat1, trip=self.trip1)

    def test_book_seat(self):
        response = self.client.post(reverse)
