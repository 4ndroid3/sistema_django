"""Modelos de Usuario y Perfil"""

# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractUser


# TODO: add login using email
# TODO: add roles to User


class Role(models.Model):
    """ Types of Roles """
    ADMIN = 1
    GERENTE = 2
    CAJERO = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (GERENTE, 'Gerente'),
        (CAJERO, 'Cajero'),
    )
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)


class User(AbstractUser):
    """ Custom User """
    role = models.ManyToManyField(Role)


class Profile(models.Model):
    """ Profile Model """
    pass
