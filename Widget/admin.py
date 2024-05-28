from django.contrib import admin
from .models import *


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ['device', 'name', 'button_type', 'status']


@admin.register(ProgressBar)
class ProgressBarAdmin(admin.ModelAdmin):
    list_display = ['device', 'name', 'value']


@admin.register(ColorStatus)
class ColorStatusAdmin(admin.ModelAdmin):
    list_display = ['device', 'name', 'value']
