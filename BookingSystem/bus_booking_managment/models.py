from django.db import models



class city(models.Model):
    name = models

class Trip(models.Model):
    start_city = models.ForeignKey(city, on_delete=models.CASCADE, related_name='meeting_point')
    end_city = models.ForeignKey(city, on_delete=models.CASCADE, related_name='destination')
    in_between_cities = models.ManyToManyField(city, related_name='between')
  

class Bus(models.Model):
    number = models
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    available_seats = models.IntegerField()

class Seat(models.Model):
    number = models.IntegerField()
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

