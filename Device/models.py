import uuid
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save


class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Room(BaseModel):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Device(BaseModel):
    room = models.ForeignKey(to=Room, related_name="room_device", on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    deviceID = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} - {self.deviceID}"


@receiver(pre_save, sender=Device)
def createDeviceId(sender, instance, **kwargs):
    if not instance.pk:
        instance.deviceID = instance.room.name + "/" + instance.name + "/" + str(uuid.uuid4()).split("-")[0]
