from django.contrib import admin

from .models import UserModel


@admin.register(UserModel)
class AdminUser(admin.ModelAdmin):
    pass
