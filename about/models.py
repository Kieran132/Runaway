from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

SERVICE_CHOICES = (
    ("Brewery Tour", "Brewery Tour"),
    )

TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)


class Appointment(models.Model):
    """
    Represents an appointment for a service.
    Each appointment is associated with a user, a selected service, a specific day,
    and a preferred time.
    Attributes:
        user (User): The user who made the appointment.
        service (str): The selected service for the appointment.
        day (datetime.date): The date of the appointment.
        time (str): The preferred time of the appointment.
    Methods:
        __str__(): Returns a string representation of the appointment.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES,
                               default="Brewery Tour")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES,
                            default="3 PM")

    def __str__(self):
        return f"{self.user} | day: {self.day} | time: {self.time}"
