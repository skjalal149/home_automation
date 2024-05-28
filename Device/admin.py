from django.contrib import admin
from .models import *


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['room', 'name', 'deviceID']
