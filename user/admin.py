from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin
from user.models import User, PhoneNumber
# Register your models here.
class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1
#
class UserAdmin(_UserAdmin):
    inlines = (PhoneNumberInline,)
#
admin.site.register(User, UserAdmin)