from django.shortcuts import render
from django.http import HttpResponse

def restaurant_home(request):
    return render(request, 'restaurant/home.html')
