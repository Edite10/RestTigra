from django.contrib import admin
from .models import Room, Booking

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'room_type', 'price', 'available')  # Columns shown in list
    list_filter = ('room_type', 'available')                      # Filter sidebar
    search_fields = ('number',)                                   # Search bar
    ordering = ('number',)                                        # Default sort

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'room', 'check_in', 'check_out')
    list_filter = ('check_in', 'check_out')
    search_fields = ('customer_name',)
    ordering = ('-check_in',)

class BookingAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)   