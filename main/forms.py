from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class NewUrlForm(forms.Form):

    url = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'class': 'form-field',
                'placeholder': 'https://discord.com/'
            }
        )
    )

class EditUrlForm(forms.Form):
    title = forms.CharField(
        required=True,
        label=('Nice'),    
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'class': 'form-field',
            }
        )
    )
    urlName = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'class': 'form-field',
            }
        )
    )
    url = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'class': 'form-field',
            }
        )
    )