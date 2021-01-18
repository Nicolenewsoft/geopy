from django import forms


class FormAddress(forms.Form):
    address = forms.CharField(label='Endereço', max_length=50)
