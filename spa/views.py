from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def spa_home(request):
    return HttpResponse("Welcome to the spa!")
