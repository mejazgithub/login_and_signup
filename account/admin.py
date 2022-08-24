from django.contrib import admin
from .views import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

# Register your models here.

class BaseUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('first_name','last_name', 'password')}),
        (_('Personal info'), {'fields': ('is_owner', 'email','profile_picture')}),
        (_('Permissions'), {
            'fields': ('is_approved','is_active', 'is_staff','is_verified','is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    filter_horizontal = ()
    ordering = ('pk',)
    list_display = ('email', 'first_name','last_name', 'is_staff')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),)

admin.site.register(User,BaseUserAdmin)

