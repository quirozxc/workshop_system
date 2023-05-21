from django import forms

class RepairOrderForm(forms.Form):
    client_first_name = forms.CharField(
        label='Nombre del Cliente',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Cliente'})
    )
    client_last_name = forms.CharField(
        label='Apellido del Cliente',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido del Cliente'})
    )