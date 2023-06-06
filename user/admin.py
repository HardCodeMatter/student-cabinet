from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import User

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('__str__', 'email', 'type')
    list_filter = ('last_name', 'first_name', 'email', 'type')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'phone',
            'photo',
        )}),
        ('Permissions', {'fields': (
            'date_joined',
            'is_staff',
            'is_active',
            'is_verified',
        )}),
        ('University information', {'fields': (
            'type',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('last_name', 'first_name', 'email')
    ordering = ('last_name',)
    filter_horizontal = ()
