from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'age')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'age', 'username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ['email', 'username']


admin.site.register(CustomUser, CustomUserAdmin)
