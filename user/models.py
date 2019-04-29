from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class CustomUser(AbstractUser):
    # add additional fields in here
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    DOB = models.DateField(default=now, null=True)
    FB = models.URLField(max_length=100)

    picture = models.ImageField(upload_to='images/')

    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=11, default=0)

    def __self__(self):
        return self.username
