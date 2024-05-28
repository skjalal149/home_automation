from rest_framework import serializers
from .models import *
from Widget.Serializer import ButtonSerializer, ProgressBarSerializer


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        exclude = ['id']


class DeviceSerializer(serializers.ModelSerializer):
    room = serializers.SlugRelatedField("uid", queryset=Room.objects.all())
    buttons = ButtonSerializer(many=True, read_only=True)
    progress = ProgressBarSerializer(many=True, read_only=True)

    class Meta:
        model = Device
        exclude = ['id']


class RoomDetailsSerializer(serializers.ModelSerializer):
    room_device = DeviceSerializer(many=True)

    class Meta:
        model = Room
        exclude = ['id']
