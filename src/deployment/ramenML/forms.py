from django import forms

from .models import NewRamen

class NewRamenForm(forms.ModelForm):
    class Meta:
        model = NewRamen
        fields = [
            'brand',
            'ingredients',
            'style',
            'country'
        ]