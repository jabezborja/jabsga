from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class NewUrlForm(forms.Form):
    title = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'class': 'form-field',
                'placeholder': 'My Title'
            }
        )
    )
    
    url_name = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'class': 'form-field',
                'placeholder': 'my_shortened_url'
            }
        )
    )

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