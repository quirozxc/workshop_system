from django.contrib import admin
from order.models import RepairOrder #, Failture
from workshop.models import Note
from workshop.models import Assignment
# Register your models here.
class NoteInline(admin.StackedInline):
    model = Note
#
class AssignmentInline(admin.TabularInline):
    model = Assignment
    extra = 1
#
class RepairOrderAdmin(admin.ModelAdmin):
    list_display = ('device', 'it_includes', 'is_active',)
    inlines = (NoteInline, AssignmentInline,)
#
admin.site.register(RepairOrder, RepairOrderAdmin)
#
#class FailtureAdmin(admin.ModelAdmin):
#    pass
#
#admin.site.register(Failture, FailtureAdmin)