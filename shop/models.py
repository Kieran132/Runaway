from django.db import models


class Category(models.Model):
    """
    Represents a category for products in the store.

    Fields:
    - name: The name of the category.
    - friendly_name: An optional user-friendly name for the category.

    Methods:
    - __str__: Returns the name of the category.
    - get_friendly_name: Returns the friendly name of the category.
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Represents a product available in the store.

    Fields:
    - category: A ForeignKey to the Category model, associating the product
      with a category.
    - sku: The Stock Keeping Unit for the product.
    - name: The name of the product.
    - description: A detailed description of the product.
    - has_sizes: A boolean indicating if the product has different sizes.
    - price: The price of the product.
    - image_url: A URL to an external image of the product.
    - image: An image file of the product stored locally.

    Methods:
    - __str__: Returns the name of the product.
    """
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
