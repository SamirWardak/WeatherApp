from django import forms
from django.forms import ModelForm, TextInput

from .models import City

class CityForm(ModelForm):
    actions_choice = [
        ('save', 'Save'),
        ('remove', 'Remove'),
        ('remove_all', 'Remove All')
    ]
    actions = forms.ChoiceField(choices=actions_choice, widget=forms.RadioSelect)

    class Meta:
        model = City
        fields = ['name', 'actions']
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'city',
                    'id': 'city',
                    'placeholder': 'Введите город'
                }
            ),
            'actions': TextInput(
                attrs={
                    'class': 'form-control',
                    'name': 'actions',
                    'id': 'actions'
                }
            )
        }
