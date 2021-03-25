# Python imports
from datetime import date
# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# from django.contrib.admin import ModelAdmin

from .models import Profile
from .models import Role


User = get_user_model()


class RoleInline(admin.StackedInline):
    model = Role
    can_delete = False
    varbose_name_plural = 'Roles'


class ProfileInline(admin.StackedInline):
    """Profile Inline. (with the user in admin page)."""
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfil'
    fk_name = 'id_users'


class CustomUserAdmin(UserAdmin):
    """Custom User Admin, add the inline profile"""
    inlines = (ProfileInline,)
    list_display = ('username', 'birth_date', 'age')
    # agregamos los roles a los filtros
    list_filter = ('profile__roles',) + UserAdmin.list_filter 

    def birth_date(self, obj):
        """Get the birth date from profile, so we can use it in list display"""
        return obj.profile.birth_date

    def age(self, obj):
        """Calculate the age from the birth date in profile"""
        today = date.today()
        return today.year - obj.profile.birth_date.year - ((today.month, today.day) < (obj.profile.birth_date.month, obj.profile.birth_date.day))

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# class CustomProfileAdmin(admin.ModelAdmin):
#     """ Custom display of elements in the admin page"""

#     list_display = ('id_users', 'birth_date',)

admin.site.register(Role)
admin.site.register(User, CustomUserAdmin)
