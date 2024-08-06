from django.db import models

# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date}"
