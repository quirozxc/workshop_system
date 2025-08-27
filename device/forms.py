from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre',
        },)
        self.fields['brand'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Marca',
        },)
        self.fields['model'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Modelo',
        },)
        self.fields['serial'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Serial',
        },)
        #
    #
    class Meta:
        model = Device
        fields = ['name', 'brand', 'model', 'serial',]
        labels = {
            'name': 'Nombre',
            'brand': 'Marca',
            'model': 'Modelo',
            'serial': 'Serial',
        }
    #
#