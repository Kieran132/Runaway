from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .forms import UserProfileForm
from .models import UserProfile

from checkout.models import Order


def profile(request):
    """
    View function to display the user's profile page and handle profile
    updates.

    This view retrieves the user's profile based on the currently
    authenticated user.
    If the request method is POST, it attempts to update the user's profile
    using the submitted form data. If the form is valid, the profile is
    updated and a success message is displayed. If the form is not valid,
    an error message is shown. If the request method is GET, the profile
    form is displayed with the user's current profile information. The
    user's order history is also fetched and displayed.

    Args:
        request: The HTTP request object.

    Returns:
        A rendered HTML template displaying the user's profile page with the
        profile form and order history.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed, please check form is'
                           'filled in correctly')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profile/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    View function to display a past order confirmation page.

    This view retrieves a specific order based on the provided order number.
    It displays a confirmation message indicating that the page is a past
    order confirmation and provides the order information. This view is
    typically accessed from the user's profile page.

    Args:
        request: The HTTP request object.
        order_number: The order number of the specific order to be displayed.

    Returns:
        A rendered HTML template displaying a past order confirmation page
        with the order details and a confirmation message.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
