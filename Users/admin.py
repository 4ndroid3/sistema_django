""" Users Admin"""

# Django Imports
from django.contrib import admin

# Project Imports
from .models import Profile

class CustomProfileAdmin(admin.ModelAdmin):
    """ Custom display of elements in the admin page"""

    list_display = ('id_users', 'birth_date',)

admin.site.register(Profile, CustomProfileAdmin)