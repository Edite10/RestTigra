# dashboard/models.py

from django.db import models
from django.contrib.auth.models import User

# Basic booking model
class Booking(models.Model):
    """
    Model for storing all types of bookings
    """
    SERVICE_CHOICES = [
        ('hotel', 'Hotel'),
        ('spa', 'Spa'),
        ('restaurant', 'Restaurant'),
        ('event', 'Event'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    booking_date = models.DateField()
    booking_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cancellation_reason = models.TextField(blank=True)
    
    # Hotel specific fields
    room_type = models.CharField(max_length=50, blank=True)
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)
    guests = models.PositiveSmallIntegerField(default=1)
    
    # Spa specific fields
    treatment = models.CharField(max_length=50, blank=True)
    spa_time = models.TimeField(null=True, blank=True)
    
    # Restaurant specific fields
    party_size = models.PositiveSmallIntegerField(default=2)
    seating_preference = models.CharField(max_length=20, blank=True)
    
    class Meta:
        ordering = ['-booking_date', '-booking_time']
        
    def __str__(self):
        return f"{self.get_service_type_display()} booking on {self.booking_date} by {self.user.username}"

# Create your dashboard models here if needed
# For now, we'll leave it empty
