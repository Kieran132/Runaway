from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    View to display all products, including sorting and search functionality.

    URL Parameters:
    - sort: Specifies the field to sort the products by.
    - direction: Specifies the sorting direction (asc or desc).
    - category: Specifies the category to filter products by.
    - q: Specifies the search query to filter products by name or description.

    Renders 'shop/shop.html' template with the list of products and filters.

    Returns:
    - Rendered HTML template with context.
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """
    View to display a single product's details.

    Parameters:
    - product_id: The ID of the product to display.

    Renders 'shop/shop_detail.html' template with the product details.

    Returns:
    - Rendered HTML template with context.
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'shop/shop_detail.html', context)


@login_required
def add_product(request):
    """
    View to add a new product to the store.

    Requires user authentication.

    Handles form submission to add a new product to the database.

    Renders 'shop/add_product.html' template with the product form.

    Returns:
    - Rendered HTML template with context.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request,
                           'Failed to add product.'
                           'Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    View to edit an existing product in the store.

    Parameters:
    - product_id: The ID of the product to edit.

    Requires user authentication.

    Handles form submission to update an existing product in the database.

    Renders 'shop/edit_product.html' template with the product form.

    Returns:
    - Rendered HTML template with context.
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('edit_product', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.'
                           'Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'shop/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    View to delete a product from the store.

    Parameters:
    - product_id: The ID of the product to delete.

    Requires user authentication.

    Deletes the specified product from the database.

    Redirects to the 'products' view after successful deletion.

    Returns:
    - Redirect response.
    """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect('products')
