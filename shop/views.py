from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))
            
            queries = Q(
                name__icontains=query) | Q(
                    description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search': query,
        'current_categories': categories,
    }
    return render(request, 'shop/shop.html', context)


def shop_detail(request, shop_id):
    """ A view to show products on their own page """

    product = get_object_or_404(Product, pk=shop_id)

    context = {
        'product': product,
    }
    return render(request, 'shop/shop_detail.html', context)
