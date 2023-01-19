from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from account.models import Profile


admin.site.unregister(User)


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = ["date_joined", "last_login"]

    inlines = [ProfileInline]
