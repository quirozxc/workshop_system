from django.db import models
from device.models import Device
# Create your models here.
class Failture(models.Model):
    description = models.CharField('Description of fault', max_length=32)
    #
    class Meta:
        db_table = 'failture'
    #
    def __str__(self):
        return self.description
#
class RepairOrder(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    failture = models.ManyToManyField(Failture)
    it_includes = models.CharField('It Includes', max_length=64, null=True, blank=True)
    budget = models.DecimalField('Budget', max_digits=6, decimal_places=2, default=0)
    is_active = models.BooleanField('Is Active', default=True)
    #
    date = models.DateField('Date', auto_now_add=True)
    #
    class Meta:
        db_table = 'repair_order'
    #
    def __str__(self):
        return 'Order #%04d' % (self.pk)
#
class Note(models.Model):
    repair_order = models.OneToOneField(RepairOrder, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField('Note', max_length=512, null=True, blank=True)
    #
    class Meta:
        db_table = 'note'
    #
    def __str__(self):
        return 'Note Record #%d' % (self.pk)
#