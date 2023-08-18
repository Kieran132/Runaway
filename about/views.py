from django.shortcuts import render, redirect
from datetime import datetime, timedelta, time
from django.core.mail import send_mail
from django.conf import settings
from .models import Appointment
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required
def booking(request):
    weekdays = validWeekday(22)
    validateWeekdays = isWeekdayValid(weekdays)

    times = [
        "3 PM", "3:30 PM", "4 PM", "4:30 PM", "5 PM", "5:30 PM", "6 PM",
        "6:30 PM", "7 PM", "7:30 PM"
    ]

    # Get the available time slots based on the selected day
    available_times = {}
    for weekday in validateWeekdays:
        available_times[weekday] = checkTime(times, weekday)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        time = request.POST.get('time')

        if not is_day_and_time_available(day, time):
            messages.error(
                request, "The selected day and time are not available.")
            return redirect('booking')

        if service is None:
            messages.success(request, "Please Select A Service!")
            return redirect('booking')

        # Get the current user
        user = request.user

        # Store day, service, and time in the Django session
        request.session['day'] = day
        request.session['service'] = service
        request.session['time'] = time

        appointment = Appointment.objects.create(
            user=user,
            service=service,
            day=day,
            time=time,  # Save the selected time to the appointment model
        )

        # Send email confirmation
        subject = 'Booking Confirmation'
        message = render_to_string('confirmation/booking_confirmation.txt', {
            'appointment': appointment,
        })
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email, settings.DEFAULT_FROM_EMAIL]
        send_mail(subject, message, email_from, recipient_list)

        return render(request, 'booking_success.html', {
            'appointment': appointment,
            'times': times,
        })

    return render(request, 'booking.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'available_times': available_times,
        'times': times,
    })


def bookingSubmit(request):
    user = request.user
    times = [
        "3 PM", "3:30 PM", "4 PM", "4:30 PM", "5 PM", "5:30 PM", "6 PM",
        "6:30 PM", "7 PM", "7:30 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')
    time = request.session.get('time')

    hour = checkTime(times, day)
    if request.method == 'POST':

        date = datetime.today().date()

        if service is None:
            if day <= maxDate and day >= minDate:
                if date.weekday() in [0, 3, 5]:
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(
                                            day=day, time=time).count() < 1:
                            appointment = Appointment.objects.create(
                                user=user,
                                service=service,
                                day=day,
                                time=time,
                            )
                            # Send email confirmation
                            subject = 'Booking Confirmation'
                            message = render_to_string(
                                'email/booking_confirmation.html', {
                                    'appointment': appointment,
                                })
                            email_from = settings.DEFAULT_FROM_EMAIL
                            recipient_list = [user.email,
                                              settings.DEFAULT_FROM_EMAIL]
                            send_mail(
                                subject, message, email_from,
                                recipient_list, html_message=message)

                            return render(request, 'booking_success.html', {
                                'appointment': appointment,
                                'times': times,
                            })
                        else:
                            messages.success(
                                request,
                                "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(
                    request,
                    "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")

    return redirect('booking')


def booking_success(request, appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id)
    except Appointment.DoesNotExist:
        messages.error(request, "Invalid appointment ID")
        return redirect('booking')

    # Remove the booked day/time from the available times
    day = appointment.day.strftime('%Y-%m-%d')
    time = appointment.time
    if day in available_times and time in available_times[day]:
        available_times[day].remove(time)

    return render(request, 'booking_success.html', {
        'appointment': appointment,
    })


def is_day_and_time_available(day, time):
    # Check if the selected day and time are available
    try:
        appointment = Appointment.objects.get(day=day, time=time)
    except Appointment.DoesNotExist:
        return True

    # If the appointment exists, check if it's in the past (already booked)
    if appointment.day < timezone.now().date():
        return True

    return False


def checkTime(times, day):
    # Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    today = datetime.now()
    weekdays = []
    for i in range(days):
        x = today + timedelta(days=i)
        if x.weekday() in [3, 4, 5]:
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if dayToWeekday(j) in ['Thursday', 'Friday', 'Saturday']:
            if Appointment.objects.filter(day=j).count() < 10:
                validateWeekdays.append(j)
    return validateWeekdays


def taproom(request):
    """ A view to return the taproom information page """
    return render(request, 'taproom.html')


def delivery(request):
    """ A view to return the delivery information page """
    return render(request, 'delivery_collection.html')


def visit(request):
    """ A view to return the visit information page """
    return render(request, 'visit.html')


def trade(request):
    """ A view to return the trade information page """
    return render(request, 'trade.html')
