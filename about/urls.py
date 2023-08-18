from django.urls import path
from . import views

urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path(
        'booking_success/<int:appointment_id>/',
        views.booking_success, name='booking_success'),
    path('taproom/', views.taproom, name='taproom'),
    path('delivery/', views.delivery, name='delivery'),
    path('visit/', views.visit, name='visit'),
    path('trade/', views.trade, name='trade'),
]
