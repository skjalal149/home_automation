from django.contrib import admin
from .models import *


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']


@admin.register(Button)
class ButtonAdmin(BaseAdmin):
    list_display = ['device', 'name', 'button_type', 'status']


@admin.register(ProgressBar)
class ProgressBarAdmin(BaseAdmin):
    list_display = ['device', 'name', 'value']


@admin.register(ColorStatus)
class ColorStatusAdmin(BaseAdmin):
    list_display = ['device', 'name', 'value']
