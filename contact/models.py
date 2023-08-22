from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms


class ContactForm(forms.Form):
    """
    A contact form for users to send messages.

    This form class provides fields for users to enter their name, email, and a message.
    It is typically used for users to send inquiries or messages to the website's administrators.

    Attributes:
        name (CharField): A field for the user's name.
            Max length: 100 characters.
        email (CharField): A field for the user's email address.
            Max length: 100 characters.
        message (CharField): A field for the user's message.
            Displayed using a textarea widget.
    """
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
