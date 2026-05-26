from django import forms
from .models import Usuario, Contacto

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu mensaje...'}),
        }

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'edad', 'ciudad']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tu edad'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Santiago, Valparaíso...'}),
        }