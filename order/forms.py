from django import forms
from betterforms.multiform import MultiModelForm
from .models import RepairOrder
#
from user.forms import UserForm, PhoneNumberForm
from device.forms import DeviceForm
from workshop.forms import AssignmentForm, NoteForm

class RepairOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        #
        self.fields['failture_description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Falla o desperfecto',
        },)
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Descripción',
            'style': 'height: 100px',
        },)
        self.fields['it_includes'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Se incluye',
        },)
        self.fields['budget'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Presupuesto',
        },)
        #
    #
    class Meta:
        model = RepairOrder
        fields = ['failture_description', 'description', 'it_includes', 'budget']
        labels = {
            'failture_description': 'Falla o desperfecto',
            'description': 'Descripción',
            'it_includes': 'Se incluye',
            'budget': 'Presupuesto',
        }
    #
#
class CreateRepairOrderMultiForm(MultiModelForm):
    form_classes = {
        'user': UserForm,
        'phone_number': PhoneNumberForm,
        'device': DeviceForm,
        'repair_order': RepairOrderForm,
        'assignment': AssignmentForm,
    }
#
class UpdateRepairOrderMultiForm(CreateRepairOrderMultiForm):
    def __init__(self, *args, **kwargs):
        self.form_classes.update({
            'note': NoteForm,
        },)
        super().__init__(*args, **kwargs)
    #
#