from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookingForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

@login_required
def book_room(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            # Send confirmation email
            send_mail(
                'Booking Confirmed',
                f'Your booking at Hotel Spa is confirmed from {booking.check_in} to {booking.check_out}.',
                'your_email@gmail.com',
                [request.user.email],
                fail_silently=False,
            )
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking/book_room.html', {'form': form})
