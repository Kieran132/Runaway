from django.shortcuts import render, redirect
from datetime import datetime, timedelta, time
from django.core.mail import send_mail
from .models import Appointment
from django.contrib import messages
from django.template.loader import render_to_string


def booking(request):
    weekdays = validWeekday(22)
    validateWeekdays = isWeekdayValid(weekdays)

    times = [
        "3 PM", "3:30 PM", "4 PM", "4:30 PM", "5 PM", "5:30 PM", "6 PM", "6:30 PM", "7 PM", "7:30 PM"
    ]
    
    # Get the available time slots based on the selected day
    available_times = {}
    for weekday in validateWeekdays:
        available_times[weekday] = checkTime(times, weekday)   

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        time = request.POST.get('time')  # Retrieve the selected time from the form
        
        if service == None:
            messages.success(request, "Please Select A Service!")
            return redirect('booking')

        # Store day, service, and time in the Django session
        request.session['day'] = day
        request.session['service'] = service
        request.session['time'] = time

        appointment = Appointment.objects.create(
            service=service,
            day=day,
            time=time,  # Save the selected time to the appointment model
        )

        return redirect('booking_success', appointment_id=appointment.id)

    return render(request, 'booking.html', {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'available_times': available_times,
        'times': times,
    })


def bookingSubmit(request):
    user = request.user
    times = [
        "3 PM", "3:30 PM", "4 PM", "4:30 PM", "5 PM", "5:30 PM", "6 PM", "6:30 PM", "7 PM", "7:30 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')
    time = request.session.get('time')

    # Only show the time of the day that has not been selected before and the time he is editing:
    hour = checkTime(times, day)
    if request.method == 'POST':
        # Remove the following line as we're retrieving the time from the session instead
        # time_str = request.POST.get("time")
        # time = datetime.strptime(time_str, '%I %p').time()  # Convert the string to time object

        date = datetime.today().date()

        if service != None:
            if day <= maxDate and day >= minDate:
                if date.weekday() in [0, 3, 5]:  # Monday, Thursday, and Saturday have weekday values of 0, 3, and 5 respectively
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1:
                            appointment = Appointment.objects.create(
                                user=user,
                                service=service,
                                day=day,
                                time=time,
                            )
                            # Send email confirmation
                            subject = 'Booking Confirmation'
                            message = render_to_string('email/booking_confirmation.html', {
                                'appointment': appointment,
                            })
                            email_from = settings.DEFAULT_FROM_EMAIL
                            recipient_list = [user.email]
                            send_mail(subject, message, email_from, recipient_list, html_message=message)

                            return render(request, 'booking_success.html', {
                                'appointment': appointment,
                                'times': times,
                            })
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")

    return redirect('booking')


def send_email_confirmation(appointment):
    # Customize the email subject and body based on your needs
    subject = "Booking Confirmation"
    message = f"Thank you for booking {appointment.service} on {appointment.day} at {appointment.time}."
    from_email = "kiemclean@hotmail.co.uk"  # Update with your email address
    to_email = appointment.email  # Update with the user's email address

    # Send the email using Django's send_mail function
    send_mail(subject, message, from_email, [to_email])


def booking_success(request, appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id)
    except Appointment.DoesNotExist:
        messages.error(request, "Invalid appointment ID")
        return redirect('booking')

    return render(request, 'booking_success.html', {
        'appointment': appointment,
    })


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
        if x.weekday() in [3, 4, 5]:  # Thursday, Friday, and Saturday have weekday values of 3, 4, and 5 respectively
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