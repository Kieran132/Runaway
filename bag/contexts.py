from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product


def bag_contents(request):
    """
    Calculate and return bag contents and related information.

    This function calculates the contents of the shopping bag,
    including the items, their quantities, prices, and relevant totals.
    It also determines the delivery cost and the grand total,
    considering the free delivery threshold if applicable.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: A dictionary containing bag-related information including:
            - 'bag_items' (list): A list of dictionaries representing 
               bag items, including item_id, quantity, product details,
               and optionally size.
            - 'total' (Decimal): The total cost of items in the bag.
            - 'product_count' (int): The total count of products in the bag.
            - 'delivery' (Decimal): The calculated delivery cost.
            - 'free_delivery_delta' (Decimal): The remaining amount required 
               to qualify for free delivery.
            - 'free_delivery_threshold' (Decimal): The threshold amount 
               for free delivery.
            - 'grand_total' (Decimal): The total cost including items
               and delivery.
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })

    if total < settings. FREE_DELIVERY_THRESHOLD:
        delivery = round(
            total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100), 2)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
