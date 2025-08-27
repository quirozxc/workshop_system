from django.db import models
from django.contrib.auth.models import AbstractUser, UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    #
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    #
    dni = models.PositiveIntegerField(_('Identification Document'), null=True)
    #
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    #
    class Meta:
        db_table= 'user'
    #
    def pending_assignments(self, just_guarantee=False):
        return self.assignment_set.filter(
            is_guarantee=just_guarantee,
            invoice=None,
            order__is_active=True,
            order__was_reviewed=False,
        ).order_by('id')
    #
    def pending_all_assignments(self):
        return self.assignment_set.filter(
            invoice=None,
            order__is_active=True,
            order__was_reviewed=False,
        ).order_by('id')
    #
    def reviewed_assignments(self):
        return self.assignment_set.filter(
            invoice=None,
            order__is_active=True,
            order__was_reviewed=True,
        ).order_by('id')
    #
    def invoiced_assignments(self):
        return self.assignment_set.filter(
            invoice__isnull=False,
        ).order_by('invoice__id')
    #
    def get_full_phone_number(self):
        return '+%d%d' % (
            self.phonenumber.idc,
            self.phonenumber.number,
        )
    #
    def get_whatsapp_url(self):
        return '%s%d%d' % (
            settings.WHATSAPP_URL,
            self.phonenumber.idc,
            self.phonenumber.number,
        )
    #
    def is_a_manager(self):
        return True if self.groups.filter(name=settings.MANAGER_NAME) else False
    #
    def __str__(self):
        if self.first_name and self.last_name:
            return '%s %s' % (self.first_name, self.last_name)
        elif self.username:
            return self.username
        elif self.dni:
            return 'DNI: %d' % (self.dni,)
        else:
            return 'User ID #%d' % (self.id)
#
class PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    idc = models.PositiveSmallIntegerField('International Dialing Code', default=settings.VE_CODE)
    number = models.PositiveIntegerField('Phone Number')
    is_whatsapp_number = models.BooleanField('Is Whatsapp Number', default=True)
    #
    class Meta:
        db_table = 'phone_number'
    #
    def __str__(self):
        return 'Phone Record #%s' % (self.pk)
#