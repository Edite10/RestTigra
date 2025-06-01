from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room
from dashboard.models import Booking
from datetime import datetime

@login_required
def my_hotel(request):
    return render(request, 'hotel/hotel_home.html',)

@login_required
def room_list(request):
    rooms = Room.objects.filter(available=True)
    return render(request, 'hotel/room_list.html', {'rooms': rooms})

@login_required
def book_room(request):
    # Get selected room if passed from room_list
    selected_room = None
    if request.method == 'GET' and 'room_id' in request.GET:
        room_id = request.GET.get('room_id')
        selected_room = get_object_or_404(Room, id=room_id)
    
    # Handle form submission
    if request.method == 'POST':
        # Process the booking form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        special_requests = request.POST.get('special_requests', '')
        room_id = request.POST.get('room_id')
        room_type = request.POST.get('room_type', 'standard')
        guests = int(request.POST.get('guests', 1))
        
        # Create booking in dashboard.models.Booking
        booking = Booking(
            user=request.user,
            service_type='hotel',
            booking_date=check_in,
            status='pending',
            special_requests=special_requests,
            room_type=room_type,
            check_in=check_in,
            check_out=check_out,
            guests=guests
        )
        
        # If room_id is provided, link to specific room
        if room_id:
            try:
                room = Room.objects.get(id=room_id)
                booking.room_type = room.room_type
                # You could store room_id in a JSON field or create a relation
                # For this example we'll just note it in special requests
                if special_requests:
                    booking.special_requests = f"Room #{room.number}\n\n{special_requests}"
                else:
                    booking.special_requests = f"Room #{room.number}"
            except Room.DoesNotExist:
                pass
        
        booking.save()
        
        messages.success(request, f"Thank you, {first_name}! Your booking for {check_in} to {check_out} has been received. We'll send a confirmation to {email} shortly.")
        return redirect('dashboard_home')
    
    return render(request, 'hotel/book_room.html', {
        'selected_room': selected_room,
        'user': request.user
    })
