from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('organizer', 'Event Organizer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='volunteer')
    profile_picture = models.ImageField(upload_to='profile_pics/', default='profile_pics/defaultpfp.png')

    def __str__(self):
        return f"{self.user.username}'s Profile"
