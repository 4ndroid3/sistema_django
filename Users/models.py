"""Modelos de Usuario y Perfil"""

# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """ Custom User """
    pass

class Profile(models.Model):
    """ Profile Model """
    pass