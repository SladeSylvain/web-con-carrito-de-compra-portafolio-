from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    correo = forms.EmailField(label='Correo electrónico')
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)

class RegistroForm(forms.Form):
    username = forms.CharField(max_length=50, label="Nombre de usuario")
    email = forms.EmailField(label="Correo electrónico")
    edad = forms.IntegerField(label="Edad")
    ciudad = forms.CharField(max_length=100, label="Ciudad")