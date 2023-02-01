from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    dni = models.PositiveIntegerField('Identification Document', null=True, blank=True)
    #
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    #
    class Meta:
        db_table= 'user'
    #
    def __str__(self):
        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name)
        return self.username
#
class PhoneNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idc = models.PositiveSmallIntegerField('International Dialing Code', default=settings.VE_CODE)
    number = models.PositiveIntegerField('Phone Number')
    is_whatsapp_number = models.BooleanField('Is Whatsapp Number', default=False)
    #
    class Meta:
        db_table = 'phone_number'
    #
    def __str__(self):
        return 'Phone Record #%d' % (self.pk)
#