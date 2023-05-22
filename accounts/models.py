from django.db import models
from django.contrib.auth.models import AbstractUser
from base.models import Hackathon

# Create your models here.


class CustomUserModel(AbstractUser):
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    hackathons_in = models.ManyToManyField(
        Hackathon, null=True, blank=True, related_name='hackathons')

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
