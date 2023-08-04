from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ["username", "email", "role"]
    list_display = ["username", "email", "role"]


admin.site.register(User, UserAdmin)
