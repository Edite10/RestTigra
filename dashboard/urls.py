# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('book/', views.book_service, name='book_service'),
    path('edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]
