from django import forms
from .models import *


class ColorModelForm(forms.ModelForm):
    code = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'type': 'color'}))

    class Meta:
        model = ColorModel
        fields = '__all__'
