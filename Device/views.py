from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .Serializer import *
from rest_framework.permissions import IsAuthenticated
from Widget.Serializer import *
from rest_framework.authentication import TokenAuthentication


class RoomView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = "uid"
    http_method_names = ['get']


class DeviceView(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = "room__uid"
    http_method_names = ['get']


class RoomDetailView(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomDetailsSerializer
    lookup_field = "room__uid"
    http_method_names = ['get']
