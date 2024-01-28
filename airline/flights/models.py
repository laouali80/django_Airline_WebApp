from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    # related_name="" this implies that we access the relationship in the reverse order that mean via the name "departures/arrivals" we can have all the flight with the origin
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    # flights show that a passenger can have many flight and vice versa
    # blank=True means to allow a passenger with no flight so a passenger can be without a flight
    # related_name means if a have a passenger a can get all his flight and also if a have a "flight" a can use a 'passengers' to get all the passengers
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
