from django.contrib import admin
from .models import SpaService, SpaBooking

@admin.register(SpaBooking)
class SpaBookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'service', 'date', 'time')
    list_filter = ('service', 'date')
    search_fields = ('customer_name',)
    ordering = ('-date', 'time')