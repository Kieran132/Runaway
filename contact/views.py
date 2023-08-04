from django.shortcuts import render, redirect
from .models import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def contact(request):
    """
    Function obtains the users input fields then uses Google smtp backend
    server to send the information to an external email
    """
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        email_from = settings.DEFAULT_FROM_EMAIL

        send_mail(
            'Contact Form Submission from {}'.format(name + ', ' + email),
            message,
            email,
            ['runawayci23@gmail.com'],
            fail_silently=False,
        )

        messages.success(
            request,
            'Thank you for submitting! Someone will be in touch!')

    return render(request, 'contact.html')