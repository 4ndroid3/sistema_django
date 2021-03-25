"""Users and Profile models"""

# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


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

    def __str__(self):
        return self.get_id_display() # display the label instead of the id number


class User(AbstractUser):
    """ Custom User."""
    pass


class Profile(models.Model):
    """ Profile Model 
    
    Personal data about Users,
    Fields:
    - id_user (OneToOneField to 'User')
    - birth_date (DateField)
    - profile_img (ImageField)
    - biography (TextField)
    """
    
    id_users = models.OneToOneField(
        User,
        default = None,
        on_delete = models.CASCADE,
        help_text = 'User name / Account name',
        verbose_name = 'User',
        related_name='profile',
    )

    roles = models.ManyToManyField(Role, related_name='profiles', blank=True)

    birth_date = models.DateField(
        blank = True,
        null=True,
        verbose_name = 'Birth date',
        help_text = 'Date of birth',
    )

    biography = models.TextField(
        default = '',
        max_length = 500,
        blank=True,
        help_text = 'Short resume or history about the User',
        verbose_name = 'Biography',
    )

    profile_img = models.ImageField(
        upload_to = 'profile_img', 
        blank = True,
        null=True,
        help_text = 'An image of the user',
        verbose_name = 'Profile Image',
    )

    def __str__(self):
        return str(self.id_users)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
