from django.contrib import admin
from order.models import RepairOrder
# Register your models here.
class RepairOrderAdmin(admin.ModelAdmin):
    pass
#
admin.site.register(RepairOrder, RepairOrderAdmin)