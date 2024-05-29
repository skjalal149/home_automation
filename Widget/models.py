import uuid
from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


BUTTON_TYPE = (("S", "SWITCH"), ("P", "PUSH BUTTON"))


class Button(BaseModel):
    device = models.OneToOneField("Device.Device", on_delete=models.CASCADE, related_name="buttons")
    name = models.CharField(max_length=255)
    button_type = models.CharField(max_length=1, choices=BUTTON_TYPE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProgressBar(BaseModel):
    device = models.OneToOneField("Device.Device", on_delete=models.CASCADE, related_name="progress")
    name = models.CharField(max_length=255)
    value = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class ColorStatus(BaseModel):
    device = models.OneToOneField("Device.Device", on_delete=models.CASCADE, related_name="color")
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=9)

    def __str__(self):
        return self.name
