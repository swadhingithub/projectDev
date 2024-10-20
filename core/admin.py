from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Inherit from UserAdmin
from unfold.admin import ModelAdmin  # Use the correct class from unfold.admin

from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin, ModelAdmin):
    # Customize fields to display in the admin panel
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Group fields for better organization
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password'),
        }),
        ('Personal Information', {
            'fields': ('first_name', 'last_name',),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined'),
        }),
    )

    # Make password field read-only (security precaution)
    readonly_fields = ('last_login', 'date_joined')

    # Add fields for creating and updating users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    

