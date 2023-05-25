from django import forms
from django.conf import settings
from user.models import User
from .models import Assignment, Note

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