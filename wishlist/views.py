from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist
from shop.models import Product


@login_required
def wishlist(request):
    # Fetch the user's wishlist
    wishlist = Wishlist.objects.filter(user=request.user)

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    This function allows the user to add their chosen product to their wishlist
    by using information from the Product model. Once added, a pop-up message
    appears telling the user they have added a product.
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
    """ Deletes product for the users wishlist """

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted successfully.')
    return redirect(reverse('wishlist'))
