from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class CustomUser(AbstractUser):
    # add additional fields in here
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    DOB = models.DateField(default=now)
    FB = models.URLField(max_length=60)
    picture = models.ImageField()
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=11, default=0)
