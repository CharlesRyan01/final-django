from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbn = models.IntegerField()
    