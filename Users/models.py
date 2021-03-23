"""Users and Profile models"""

# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractUser

# Project Imports

class User(AbstractUser):
    """ Custom User """
    pass

class Profile(models.Model):
    """ Profile Model """
    pass