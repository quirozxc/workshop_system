from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    dni = models.PositiveIntegerField('Identification Document', null=True, blank=True)
    #
    class Meta:
        db_table= 'user'
    #
#
class PhoneNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idc = models.PositiveSmallIntegerField('International Dialing Code', default=settings.VE_CODE)
    operator = models.CharField('Operator Identifier', max_length=1, choices=settings.VE_OPERATOR)
    number = models.PositiveIntegerField('Phone Number')
    is_whatsapp_number = models.BooleanField('Is Whatsapp Number', default=False)
    #
    class Meta:
        db_table = 'phone_number'
    #
#