"""Users and Profile models"""

# Django Imports
from django.db import models
from django.contrib.auth.models import AbstractUser

# Project Imports

class User(AbstractUser):
    """ Custom User """
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
        'User',
        on_delete = models.CASCADE,
        help_text = 'User name / Account name',
        verbose_name = 'User',
    )
