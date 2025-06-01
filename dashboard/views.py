# dashboard/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking

@login_required
def dashboard_home(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'dashboard/home.html', {'bookings': bookings})


@login_required
def edit_booking(request, booking_id):
    """
    Edit an existing booking
    """
    # Get the booking, ensuring it belongs to the current user
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        # Handle the form submission
        booking.booking_date = request.POST.get('booking_date')
        if request.POST.get('booking_time'):
            booking.booking_time = request.POST.get('booking_time')
        booking.special_requests = request.POST.get('special_requests', '')
        
        # Additional fields based on service type
        if booking.service_type == 'hotel':
            # Process hotel-specific fields
            pass  # Implement based on your Booking model
        elif booking.service_type == 'spa':
            # Process spa-specific fields
            pass  # Implement based on your Booking model
        elif booking.service_type == 'restaurant':
            # Process restaurant-specific fields
            pass  # Implement based on your Booking model
            
        booking.save()
        messages.success(request, f"Your {booking.service_type} booking has been updated successfully.")
        return redirect('dashboard_home')
    
    # For GET request, prepare context data
    context = {'booking': booking}
    
    # Add service-specific details
    if booking.service_type == 'hotel':
        # Add hotel booking details
        context['hotel_details'] = {
            'room_type': getattr(booking, 'room_type', 'Standard'),
            'check_in': getattr(booking, 'check_in', ''),
            'check_out': getattr(booking, 'check_out', ''),
        }
    elif booking.service_type == 'spa':
        # Add spa booking details
        context['spa_details'] = {
            'treatment': getattr(booking, 'treatment', 'Massage'),
            'spa_time': getattr(booking, 'spa_time', ''),
        }
    elif booking.service_type == 'restaurant':
        # Add restaurant booking details
        context['restaurant_details'] = {
            'party_size': getattr(booking, 'party_size', 2),
            'seating_preference': getattr(booking, 'seating_preference', 'any'),
        }

    return render(request, 'dashboard/edit_booking.html', context)

@login_required
def cancel_booking(request, booking_id):
    """
    Cancel a booking
    """
    # Get the booking, ensuring it belongs to the current user
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        # Check if confirmation was provided
        if request.POST.get('understand'):
            # Update booking status to cancelled
            booking.status = 'cancelled'
            # Store cancellation reason if provided
            reason = request.POST.get('reason', '')
            if reason:
                booking.cancellation_reason = reason
            booking.save()
            
            messages.success(request, f"Your {booking.service_type} booking has been cancelled successfully.")
            return redirect('dashboard_home')
        else:
            messages.error(request, "You must acknowledge the cancellation policy to proceed.")
    
    return render(request, 'dashboard/cancel.html', {
        'booking': booking
    })

@login_required
def dashboard_view(request):
    """
    Display all bookings for the currently logged-in user
    """
    # Get bookings only for the current user
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    
    return render(request, 'dashboard/home.html', {
        'bookings': bookings
    })

@login_required
def book_service(request):
    """
    View to select which service to book
    """
    return render(request, 'dashboard/book_service.html')
