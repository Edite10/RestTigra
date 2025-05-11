from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# Create your views here.

def my_hotel(request):
    return HttpResponse("Welcome to Rest Tigra!")

def room_list(request):
    rooms = Room.objects.filter(available=True)
    return render(request, 'booking/room_list.html', {'rooms': rooms})
