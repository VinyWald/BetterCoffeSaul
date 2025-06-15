# home/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        # Ajuste os campos conforme necessário. Remova 'first_name', 'last_name' se não quiser pedi-los.
        fields = ('username',) # Ou apenas ('username', 'email')



class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
        min_value=0, 
        max_value=5, 
        widget=forms.HiddenInput() # O input será escondido, usaremos CSS e JS para as estrelas
    )
    
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Deixe seu comentário aqui...'}),
        }
        labels = {
            'comment': 'Comentário',
        }