from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
#
from datetime import timedelta
#
from order.models import RepairOrder
from user.models import User
# Create your models here.
class Assignment(models.Model):
    order = models.ForeignKey(RepairOrder, on_delete=models.CASCADE)
    delegate = models.ForeignKey(User, on_delete=models.RESTRICT)
    is_guarantee = models.BooleanField('Is Guarantee', default=False)
    #
    date = models.DateField('Date', auto_now_add=True)
    #
    class Meta:
        db_table = 'assignment'
    #
    def get_all_pending():
        return Assignment.objects.filter(
            invoice=None,
            order__is_active=True,
            order__was_reviewed=False,
        ).order_by('id')
    #
    def get_all_reviewed():
        return Assignment.objects.filter(
            invoice=None,
            order__is_active=True,
            order__was_reviewed=True,
        ).order_by('id')
    #
    def get_all_invoiced():
        return Assignment.objects.filter(
            invoice__isnull=False,
        ).order_by('invoice__id')
    #
    def __str__(self):
        return 'Assignment Record #%s' % (self.pk)
    #
    def get_update_order_url(self):
        return reverse('update_order', kwargs={'pk': self.pk})
    #
    def get_create_invoice_url(self):
        return reverse('create_invoice', kwargs={'pk': self.pk})
    #
    def get_update_invoice_url(self):
        return reverse('update_invoice', kwargs={'pk': self.pk})
    #
    def get_delete_invoice_url(self):
        return reverse('delete_invoice', kwargs={'pk': self.pk})
    #
    def get_create_guarantee_url(self):
        return reverse('create_guarantee', kwargs={'pk': self.pk})
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
    @property
    def was_picked(self):
        if self.pickup_date:
            return True
        return False
    #
    class Meta:
        db_table = 'invoice'
    #
    def get_note_or_none(self):
        if hasattr(self, 'note'):
            return self.note.note
        return None
    #
    def can_apply_for_warranty(self):
        if self.pickup_date:
            if self.pickup_date + timedelta(days=self.warranty_days) >= timezone.now().date():
                return True
            #
        return False
    #
    def __str__(self):
        return 'Invoice Record #%s' % (self.pk)
    #
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