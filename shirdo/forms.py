from django import forms
from .models import Do

class DoForm(forms.ModelForm):
    class Meta:
        model = Do
        fields = ['item','completed']