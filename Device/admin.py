from django.contrib import admin
from .models import *


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at']


@admin.register(Room)
class RoomAdmin(BaseAdmin):
    list_display = ['name']


@admin.register(Device)
class DeviceAdmin(BaseAdmin):
    list_display = ['room', 'name', 'deviceID']
