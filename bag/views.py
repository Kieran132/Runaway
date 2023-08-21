from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages


def view_bag(request):
    """ A view to return the shopping bag page """
    return render(request, 'bag/bag.html')


def adjust_bag(request, item_id):
    """ Adjust quantity of the specified product to the shopping bag """

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
    """ Add a quantity of the specified product to the shopping bag """

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
    """Remove the item from the shopping bag"""

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
