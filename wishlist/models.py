from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class Wishlist(models.Model):
    """
    Model representing a user's wishlist item.

    Fields:
    - user: The user who owns the wishlist item.
    - product: The product associated with the wishlist item.

    Relationships:
    - user: ForeignKey to the User model representing the owner of the 
            wishlist item.
    - product: ForeignKey to the Product model representing the product in the 
               wishlist.

    Attributes:
    - user: The user who owns the wishlist item.
    - product: The product associated with the wishlist item.

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE, null=True,
                                blank=True)
