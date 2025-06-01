from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def restaurant_home(request):
    # This page can be viewed without login
    return render(request, 'restaurant/restaurant_home.html')

@login_required
def book_table(request):
    # ...existing code...
    return render(request, 'restaurant/book_table.html')
