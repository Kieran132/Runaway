from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Form class for creating and updating product instances.

    This form class is used to create and update product instances based on
    the Product model. It includes all fields from the model and customizes
    the rendering of the 'category' field choices to display friendly names.
    Additionally, it applies CSS styling to the form fields for consistent
    appearance.

    Attributes:
        Meta:
            model (Product): The model associated with the form.
            fields (tuple): The fields from the model that will be included in
            the form.
                        Here, all fields from the Product model are included.
    """
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
