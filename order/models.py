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
    description = models.TextField('Description', max_length=512, null=True, blank=True)
    it_includes = models.CharField('It Includes', max_length=64, null=True, blank=True)
    budget = models.DecimalField('Budget', max_digits=6, decimal_places=2, default=0)
    # previous_amount = models.DecimalField('Previous Amount', max_digits=6, decimal_places=2, default=0)
    was_reviewed = models.BooleanField('Was Reviewed', default=False)
    is_active = models.BooleanField('Is Active', default=True)
    #
    date = models.DateField('Date', auto_now_add=True)
    #
    class Meta:
        db_table = 'repair_order'
    #
    def has_note_or_none(self):
        if hasattr(self, 'note'):
            return self.note
        return None
    #
    def __str__(self):
        return 'Order #%s' % (self.pk)
#