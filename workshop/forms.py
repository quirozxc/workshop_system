from django import forms
from django.conf import settings
from user.models import User
from .models import Assignment, Invoice, Note

class AssignmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        #
        self.fields['delegate'].queryset = User.objects.filter(groups__name=settings.DELEGATE_NAME)
        self.fields['delegate'].widget.attrs.update({
            'class': 'form-select',
            'placeholder': 'Técnico Delegado',
        },)
        self.fields['is_guarantee'].widget.attrs.update({
            'class': 'form-check-input',
            'placeholder': '¿Es una garantía?',
        },)
        #
    #
    class Meta:
        model = Assignment
        fields = ['delegate', 'is_guarantee',]
        labels = {
            'delegate': 'Técnico Delegado',
            'is_guarantee': '¿Es una garantía?',
        }
    #
#
class CreateInvoiceForm(forms.ModelForm):
    is_picked = forms.BooleanField(
        initial=False,
        required=False,
        label='¿Se entrega de inmediato?')
    note = forms.CharField(
        max_length=512,
        required=False,
        label='Nota de Facturación',
        widget=forms.Textarea(),
    )
    #
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        self.fields['assignment'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Orden Asignada',
        },)
        self.fields['amount'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Costo de la Reparación',
        },)
        self.fields['warranty_days'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Días de Garantía',
        },)
        self.fields['is_picked'].widget.attrs.update({
            'class': 'form-check-input',
            'placeholder': '¿Se entrega de inmediato?',
        },)
        self.fields['note'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nota de Facturación',
            'style': 'height: 100px',
        },)
    #
    class Meta:
        model = Invoice
        fields = ['assignment', 'amount', 'warranty_days',]
        labels = {
            'assignment': 'Orden Asignada',
            'amount': 'Costo de la Reparación',
            'warranty_days': 'Días de Garantía',
        }
        widgets = {
            'assignment': forms.HiddenInput(),
        }
#
class UpdateInvoiceForm(CreateInvoiceForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_picked'].label = 'Marcar como Entregado'
        self.fields['is_picked'].widget.attrs.update({
            'class': 'form-check-input',
            'placeholder': 'Marcar como Entregado',
        },)
    #
#
class NoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        #
        self.fields['note'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nota Técnica',
            'style': 'height: 100px',
        },)
    #
    class Meta:
        model = Note
        fields = ['note',]
        labels = {
            'note': 'Nota Técnica',
        }