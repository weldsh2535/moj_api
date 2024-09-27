from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # You can customize the fields displayed in the admin here
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('avatar', 'user_type')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('avatar', 'user_type')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
