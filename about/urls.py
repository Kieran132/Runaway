from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('booking_success/<int:appointment_id>/', views.booking_success, name='booking_success'),
]

