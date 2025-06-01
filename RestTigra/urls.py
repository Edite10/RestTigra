"""
URL configuration for RestTigra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hotel.views import my_hotel, room_list, book_room
from restaurant.views import restaurant_home
from spa.views import spa_home
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from contact.views import contact_view

urlpatterns = [
    path('',TemplateView.as_view(template_name='welcome.html'), name='home'),
    path('admin/', admin.site.urls),
    path('hotel/', my_hotel, name='my_hotel'),
    path('hotel/rooms/', room_list, name='room_list'),
    path('hotel/book/', book_room, name='book_room'),
    path('restaurant/', restaurant_home, name='restaurant_home'),
    path('spa/', spa_home, name='spa_home'),
    path('accounts/', include('allauth.urls')),
    path('events/', TemplateView.as_view(template_name='events.html'), name='events'),
    path('premises/', TemplateView.as_view(template_name='premises.html'), name='premises'),
    path('contactus/', contact_view, name='contactus'),
    path('dashboard/', include('dashboard.urls')),

]
