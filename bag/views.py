from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages


def view_bag(request):
    """
    Display the shopping bag page.

    This view renders the shopping bag page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The response rendered from the template.
    """
    return render(request, 'bag/bag.html')


def adjust_bag(request, item_id):
    """
    Adjust the quantity of a product in the shopping bag.

    This view allows users to adjust the quantity of a specified product
    in the shopping bag. It handles both quantity adjustments and removals.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the product to be adjusted.

    Returns:
        HttpResponse: The response to redirect the user after adjustment.
    """

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag

    messages.success(request, 'Product updated successfully.')

    return redirect(reverse('view_bag'))


def add_to_bag(request, item_id):
    """
    Add a quantity of a product to the shopping bag.

    This view adds a specified quantity of a product to the shopping bag.
    It also handles the addition of products with different sizes.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the product to be added.

    Returns:
        HttpResponse: The response to redirect the user after addition.
    """

    quantity_str = request.POST.get('quantity')
    if quantity_str and quantity_str.isdigit():
        quantity = int(quantity_str)
    else:
        quantity = 1
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag

    messages.success(request, 'Product added successfully.')

    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """
    Remove an item from the shopping bag.

    This view removes a specified item from the shopping bag.
    It handles both regular products and products with sizes.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the item to be removed.

    Returns:
        HttpResponse: The HTTP response status code.
            - 200: Successful removal.
            - 500: Internal server error during removal.
    """

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag

        messages.success(request, 'Product deleted successfully.')

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
