from django.contrib import admin
from .models import Table, Reservation

admin.site.register(Table)
admin.site.register(Reservation)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats', 'available')
    list_filter = ('available',)
    ordering = ('number',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'table', 'date', 'time')
    list_filter = ('date', 'table')
    search_fields = ('customer_name',)
    ordering = ('-date', 'time')
    