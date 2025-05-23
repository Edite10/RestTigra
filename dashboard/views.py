# dashboard/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm

@login_required
def dashboard_home(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'dashboard/home.html', {'bookings': bookings})

@login_required
def book_service(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('dashboard_home')
    else:
        form = BookingForm()
    return render(request, 'dashboard/book.html', {'form': form})

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('dashboard_home')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'dashboard/edit.html', {'form': form})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('dashboard_home')

@login_required
def dashboard_view(request):
    """
    Display the user dashboard showing all their bookings
    """
    # Example bookings - in a real app, you would query your database
    context = {
        'bookings': [
            {
                'id': 1,
                'type': 'Hotel',
                'details': 'Deluxe Room',
                'date': '2023-07-15 to 2023-07-17',
                'status': 'Confirmed'
            },
            {
                'id': 2,
                'type': 'Spa',
                'details': 'Massage Treatment',
                'date': '2023-07-16 14:00',
                'status': 'Pending'
            }
        ]
    }
    return render(request, 'dashboard.html', context)
