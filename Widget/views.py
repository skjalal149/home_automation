from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

STATUS = {
    True: "activate",
    False: "deactivate"
}


class ButtonView(APIView):

    def get(self, request, uid):
        btn = get_object_or_404(Button, uid=uid)
        btn.status = not btn.status
        btn.save()
        return Response({"message": f"{btn.device.name} is {STATUS[btn.status]}"})


class ProgressBarView(APIView):

    def post(self, request):
        uid = request.data['uid']
        value = request.data['value']
        btn = get_object_or_404(ProgressBar, uid=uid)
        btn.value = value
        btn.save()
        return Response({"message": f"{btn.device.name} has set to {value}"})


class ColorStatusView(APIView):

    def post(self, request):
        uid = request.data['uid']
        value = request.data['value']
        btn = get_object_or_404(ColorStatus, uid=uid)
        btn.value = value
        btn.save()
        return Response({"message": f"{btn.device.name}'s color has set to {value}"})
