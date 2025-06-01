from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def spa_home(request):
    # This page can be viewed without login
    return render(request, 'spa/spa_home.html')

@login_required
def spa_booking(request):
    # ...existing code...
    return render(request, 'spa/spa_booking.html')
