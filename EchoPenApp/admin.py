from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from .models import *


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["Username", "Email", "DateOfJoined", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["Username", "Email", "password", 'slug']}),
        ("Personal info", {"fields": ["DateOfJoined"]}),
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


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "status", "created_time"]
    list_filter = ["status"]
    ordering = ["created_time"]
    search_fields = ["title", "author__username"]  # assuming author is a ForeignKey to User model

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author', 'status')
        }),
    )


admin.site.register(Article, ArticleAdmin)
