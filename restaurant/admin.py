from django.contrib import admin
from .models import Table, Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'table', 'date', 'time')
    list_filter = ('date', 'table')
    search_fields = ('customer_name',)
    ordering = ('-date', 'time')
