from django.db import models
from children.models import Child
from camp.models import Club
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)  # Club being booked
    child = models.ForeignKey(Child, on_delete=models.CASCADE)  # Child attending
    parent = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Parent making booking
    booking_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    PAYMENT_CHOICES = [
        ('voucher', 'Voucher'),
        ('card', 'Card'),
        
    ]
    payment_status = models.CharField(max_length=10, choices=PAYMENT_CHOICES, default='pending')
    def __str__(self):
        return f"Booking for {self.child.first_name} in {self.club.name} ({self.status})"