from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User, PhoneNumber
from device.models import Device
# Register your models here.
class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1
#
class DeviceInline(admin.TabularInline):
    model = Device
    extra = 1
#
class CustomUserAdmin(UserAdmin):
    UserAdmin.fieldsets += (
        ('Unique Identifier', {
            'classes': ('wide',),
            'fields': (
                'dni',
            )}
        ),
    )
    inlines = (PhoneNumberInline, DeviceInline,)
#
admin.site.register(User, CustomUserAdmin)