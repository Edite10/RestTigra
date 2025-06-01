from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'booking_date', 'status', 'created_at')
    list_filter = ('service_type', 'status', 'booking_date')
    search_fields = ('user__username', 'user__email', 'special_requests', 'room_type')
    date_hierarchy = 'booking_date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'service_type', 'booking_date', 'booking_time', 'status')
        }),
        ('Additional Details', {
            'fields': ('special_requests', 'cancellation_reason')
        }),
        ('Hotel Booking', {
            'fields': ('room_type', 'check_in', 'check_out', 'guests'),
            'classes': ('collapse',),
        }),
        ('Spa Booking', {
            'fields': ('treatment', 'spa_time'),
            'classes': ('collapse',),
        }),
        ('Restaurant Booking', {
            'fields': ('party_size', 'seating_preference'),
            'classes': ('collapse',),
        }),
    )
