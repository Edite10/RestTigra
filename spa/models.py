from django.db import models

# Create your models here.

class SpaService(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class SpaBooking(models.Model):
    customer_name = models.CharField(max_length=100)
    service = models.ForeignKey(SpaService, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.customer_name} - {self.service.name} on {self.date} at {self.time}"