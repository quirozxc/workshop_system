from django.db import models
from django.urls import reverse
from django.conf import settings
from order.models import RepairOrder
from user.models import User
# Create your models here.
class Assignment(models.Model):
    order = models.ForeignKey(RepairOrder, on_delete=models.CASCADE)
    delegate = models.ForeignKey(User, on_delete=models.RESTRICT)
    is_guarantee = models.BooleanField('Is Guarantee', default=False)
    #
    @property
    def order_date(self):
        return self.order.date
    #
    class Meta:
        db_table = 'assignment'
    #
    def get_pendings():
        return Assignment.objects.filter(invoice=None)
    #
    def __str__(self):
        return 'Assignment Record #%s' % (self.pk)
    #
    def get_absolute_url(self):
        return reverse("update_order", kwargs={"pk": self.pk})
    #
#
class Invoice(models.Model):
    assignment = models.OneToOneField(Assignment, on_delete=models.RESTRICT)
    amount = models.DecimalField('Amount', max_digits=6, decimal_places=2, default=0)
    warranty_days = models.SmallIntegerField('Warranty Days', default=settings.DEFAULT_WARRANTY_DAYS)
    #
    creation_date = models.DateField('Creation Date', auto_now_add=True)
    pickup_date = models.DateField('Delivery Date', null=True, blank=True)
    #
    class Meta:
        db_table = 'invoice'
    #
    def __str__(self):
        return 'Invoice Record #%s' % (self.pk)
#
class Note(models.Model):
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    repair_order = models.OneToOneField(RepairOrder, on_delete=models.CASCADE, null=True, blank=True)
    note = models.TextField('Note', max_length=512, null=True, blank=True)
    #
    class Meta:
        db_table = 'note'
    #
    def __str__(self):
        return 'Note Record #%s' % (self.pk)
#