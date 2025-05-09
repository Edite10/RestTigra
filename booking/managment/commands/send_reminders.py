# booking/management/commands/send_reminders.py
from django.core.management.base import BaseCommand
from booking.models import Booking
from django.core.mail import send_mail
from datetime import timedelta, date

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        today = date.today()
        tomorrow = today + timedelta(days=1)
        bookings = Booking.objects.filter(check_in=tomorrow, email_sent=False)
        for booking in bookings:
            send_mail(
                'Upcoming Booking Reminder',
                f'Reminder: Your stay begins on {booking.check_in}.',
                'your_email@gmail.com',
                [booking.user.email],
            )
            booking.email_sent = True
            booking.save()
