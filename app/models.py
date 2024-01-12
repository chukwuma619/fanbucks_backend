from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='images/', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    job_role = models.CharField(max_length=250, null=True, blank=True)
    portfolio_link = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
