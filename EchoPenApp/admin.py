from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["Username", "Email", "DateOfJoined", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["Username", "Email", "password", 'slug']}),
        ("Personal info", {"fields": [ "DateOfJoined"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["Username", "Email", "DateOfJoined", "password1", "password2", 'slug'],
            },
        ),
    ]
    search_fields = ["Email"]
    ordering = ["Email"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
