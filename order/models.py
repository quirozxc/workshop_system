from django.db import models
from user.models import User
from device.models import Device
# Create your models here.
class Failture(models.Model):
    description = models.CharField('Description of fault', max_length=32)
    #
    class Meta:
        db_table = 'failture'
    #
#
class RepairOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    failture = models.ForeignKey(Failture, on_delete=models.CASCADE)
    note = models.CharField('Failture', max_length=256)
    class Meta:
        db_table = 'repair_order'
    #
#