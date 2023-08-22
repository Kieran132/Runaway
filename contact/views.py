from django.shortcuts import render, redirect
from .models import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def contact(request):
    """
    Process and send user-submitted contact information via email.

    This function handles the submission of a contact form by obtaining user
    input fields (name, email, and message), and then utilizes the Google
    SMTP backend server to send the information as an email to a designated
    external email address. After successfully sending the email, a success
    message is displayed to the user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response with the appropriate message.
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
