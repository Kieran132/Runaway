from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'shop/shop.html', context)


def shop_detail(request, shop_id):
    """ A view to show products on their own page """

    product = get_object_or_404(Product, pk=shop_id)

    context = {
        'product': product,
    }
    return render(request, 'shop/shop_detail.html', context)
