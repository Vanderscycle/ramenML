from django import forms

from .models import NewRamen

class NewRamenForm(forms.ModelForm):
    class Meta:
        model = NewRamen
        fields = [
            'brand',
            'style',
            'country',
            'ingredients'
        ]