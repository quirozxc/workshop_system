from django.db import models
from user.models import User
# Create your models here.
class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=32, null=True, blank=True)
    description = models.CharField('Description', max_length=128, null=True, blank=True)
    serial = models.PositiveIntegerField('Serial Number', null=True, blank=True)
    #
    class Meta:
        db_table = 'device'
    #
#