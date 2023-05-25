from django.contrib import admin
from device.models import Device
# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'date')
#
admin.site.register(Device, DeviceAdmin)