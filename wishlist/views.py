from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist
from shop.models import Product


@login_required
def wishlist(request):
    """
    Display the user's wishlist containing their saved products.

    Retrieves the wishlist items associated with the currently logged-in user
    and renders the 'wishlist.html' template to display the list of wishlist
    items.

    Context:
    - wishlist: Queryset containing the wishlist items for the user.

    """
    wishlist = Wishlist.objects.filter(user=request.user)

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist.

    If the product is not already in the user's wishlist, it is added to
    the wishlist.
    If the product is already in the wishlist, a warning message is displayed.
    After adding the product, a success message is shown to the user.

    Parameters:
    - product_id: The ID of the product to be added to the wishlist.

    Redirects:
    - After processing, redirects the user back to the 'wishlist' page.

    """
    user = request.user
    product = get_object_or_404(Product, id=product_id)

    # Check if the item already exists in the user's wishlist
    item_exists = Wishlist.objects.filter(user=user, product=product).exists()

    if item_exists:
        messages.warning(request, "This item is already in your wishlist.")
    else:
        wishlist = Wishlist(user=user, product=product)
        wishlist.save()
        messages.success(request, "Item added to wishlist successfully.")

    return redirect('wishlist')


@login_required
def delete_wishlist_product(request, product_id):
    """
    Remove a product from the user's wishlist.

    If the product is in the user's wishlist and the request is valid,
    the product is removed from the wishlist and a success message is
    displayed. If the request is invalid, an error message is displayed.

    Parameters:
    - product_id: The ID of the product to be removed from the wishlist.

    Redirects:
    - After processing, redirects the user back to the 'wishlist' page.

    """

    product = get_object_or_404(Product, pk=product_id)
    
    wishlist_item = get_object_or_404(
        Wishlist, user=request.user, product=product)

    if request.GET.get('from_wishlist_page') == 'true':
        wishlist_item.delete()
        messages.success(request, 'Product deleted successfully.')
    else:
        messages.error(request, 'Invalid request to delete product.')

    return redirect('wishlist')
