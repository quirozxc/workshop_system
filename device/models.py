from django.db import models
from user.models import User
# Create your models here.
class Device(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner')
    name = models.CharField('Name', max_length=32)
    brand = models.CharField('Brand', max_length=32, null=True, blank=True)
    model = models.CharField('Model', max_length=32, null=True, blank=True)
    serial = models.PositiveIntegerField('Serial Number', null=True, blank=True)
    #
    date = models.DateField('Date', auto_now_add=True)
    #
    class Meta:
        db_table = 'device'
    #
    def get_resume(self):
        return '%s: %s, %s, %s.' % (
            self.name,
            self.brand or 'no se registro marca',
            self.model or 'no se registro modelo',
            self.serial or 'sin serial',
        )
    def __str__(self):
        return 'Name: %s - Owner: %s' % (self.name, self.owner)
#