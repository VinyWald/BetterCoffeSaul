from django import forms
from . models import Cardapio

class CarForm(forms.ModelForm):
    class Meta:
        model= Cardapio
        fields= '__all__'