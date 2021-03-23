from Users.models import Role, User
from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from .models import Role, User


admin.site.register(Role)
admin.site.register(User, ModelAdmin)

# we may also need to modify this in order to 
# atach the user profile to the user in the 
# admin page