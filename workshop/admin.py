from django.contrib import admin
from workshop.models import Assignment, Invoice, Note
# Register your models here.
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('order', 'delegate', 'is_guarantee', 'date')
    #
admin.site.register(Assignment, AssignmentAdmin)
#
class NoteInline(admin.StackedInline):
    model = Note
#
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('assignment', 'amount', 'warranty_days', 'creation_date', 'pickup_date',)
    inlines = (NoteInline,)
#
admin.site.register(Invoice, InvoiceAdmin)