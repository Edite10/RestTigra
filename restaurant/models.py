from django.db import models

# Create your models here.

class Table(models.Model):
    number = models.PositiveIntegerField()
    seats = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"

class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Reservation for {self.customer_name} on {self.date} at {self.time}"