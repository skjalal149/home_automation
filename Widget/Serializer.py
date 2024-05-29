from rest_framework import serializers
from .models import *
from Device.models import Device


class ButtonSerializer(serializers.ModelSerializer):
    device = serializers.SlugRelatedField(slug_field="uid", queryset=Device.objects.all())

    class Meta:
        model = Button
        exclude = ['id']


class ProgressBarSerializer(serializers.ModelSerializer):
    device = serializers.SlugRelatedField(slug_field="uid", queryset=Device.objects.all())

    class Meta:
        model = ProgressBar
        exclude = ['id']


class ColorStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorStatus
        exclude = ['id']
