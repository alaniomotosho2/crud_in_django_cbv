from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
            'class':'form-control input-md',
            'style': 'width: 100%; display: inline;',
        }),required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
            'class':'form-control input-md',
            'style': 'width: 100%; display: inline;',
        }),required=True)
    class Meta:
        model = Person
        fields = ['first_name','last_name']