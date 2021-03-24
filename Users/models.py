"""Users and Profile models"""

# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Project Imports

# class User(AbstractUser):
#     """ Custom User """
#     pass

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
    )

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
        help_text = 'A image of the user',
        verbose_name = 'Profile Image',
    )

    def __str__(self):
        return str(self.id_users)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'