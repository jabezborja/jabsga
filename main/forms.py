from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class NewUrlForm(forms.Form):

    url = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'mt-7 focus:ring-indigo-500 focus:border-indigo-500 block w-full h-10 pl-7 pr-12 sm:text-sm border-gray-300 rounded-md',
                'placeholder': 'https://discord.com/'
            }
        )
    )

class EditUrlForm(forms.Form):
    title = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                'id': 'txtt',
                'class': 'form-control form-field',
                'type': 'text'
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
    