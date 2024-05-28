from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .Serializer import *
from rest_framework.permissions import IsAdminUser
from Widget.Serializer import *


class RoomView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [IsAdminUser]


class DeviceView(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    # permission_classes = [IsAdminUser]
