# dashboard/models.py

from django.db import models
from django.conf import settings

# Basic booking model
class Booking(models.Model):
    SERVICE_CHOICES = [
        ('hotel', 'Hotel'),
        ('spa', 'Spa'),
        ('restaurant', 'Restaurant'),
        ('event', 'Event Space'),
        ('premises', 'Premises'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    booking_date = models.DateField()
    booking_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.service_type} booking on {self.booking_date} by {self.user.username}"

# Create your dashboard models here if needed
# For now, we'll leave it empty
