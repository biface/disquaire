"""
    forms
    =====

    This file is dedicated to forms paraméters controls

"""

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Nom',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True
    )

