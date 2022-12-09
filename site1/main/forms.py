from .models import Person
from django.forms import  ModelForm, TextInput, NumberInput


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ["name", "phoneNumber"]
        widgets = {
            "name": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя'
            }),
            "phoneNumber": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер'
            }),
        }