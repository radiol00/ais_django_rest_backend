from django.contrib import admin
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    fields = ['is_staff', 'is_active']


admin.site.register(CustomUser, CustomUserAdmin)