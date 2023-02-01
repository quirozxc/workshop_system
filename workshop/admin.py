from django.contrib import admin
from workshop.models import Assignment, Invoice, Consideration
# Register your models here.
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('order', 'delegate', 'is_guarantee', 'order_date')
    #
admin.site.register(Assignment, AssignmentAdmin)
#
class ConsiderationInline(admin.StackedInline):
    model = Consideration
#
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'amount', 'warranty_days', 'creation_date', 'delivery_date',)
    inlines = (ConsiderationInline,)
#
admin.site.register(Invoice, InvoiceAdmin)