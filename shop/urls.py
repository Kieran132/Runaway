from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<shop_id>', views.shop_detail, name='shop_detail'),
]
