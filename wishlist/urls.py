from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete_wishlist_product/<int:product_id>/', views.delete_wishlist_product, name='delete_wishlist_product'),
]
