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
    # PASO 1: Creamos el campo password explícitamente para usar el widget de Ocultar Texto
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Crea una contraseña segura'}),
        label="Contraseña"
    )

    class Meta:
        model = Usuario
        # PASO 2: Agregamos 'password' a la lista de campos (fields)
        fields = ['username', 'email', 'edad', 'ciudad', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre de usuario'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'tu@email.com'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tu edad'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Santiago, Valparaíso...'}),
        }

    # PASO 3: Agregamos la validación "clean" para proteger la contraseña (mínimo 6 caracteres)
    def clean_password(self):
        # Regla: Leer el dato limpio
        password = self.cleaned_data.get('password')
        
        # Regla: Validar la longitud
        if password and len(password) < 6:
            raise forms.ValidationError('La contraseña debe tener al menos 6 caracteres.')
            
        # Regla: SIEMPRE retornar el valor analizado
        return password