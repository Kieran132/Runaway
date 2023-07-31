from django.shortcuts import render, redirect
from .models import ContactForm
from django.core.mail import send_mail
from django.contrib import messages


def contact(request):
    """
    Function obtains the users input fields then uses Google smtp backend
    server to send the information to an external email
    """
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'Contact Form Submission from {}'.format(name + ', ' + email),
            message,
            email,
            ['kiemclean11@gmail.com'],
            fail_silently=False,
        )

        print('working')

        messages.success(
            request,
            'Thank you for submitting! Someone will be in touch!')

    return render(request, 'contact.html')