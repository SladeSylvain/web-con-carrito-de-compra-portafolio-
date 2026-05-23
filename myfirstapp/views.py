from django.shortcuts import render, redirect
from .forms import ContactForm, RegistroForm
from .models import Contacto, Usuario

# Create your views here.

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']
            
            Contacto.objects.create(
                name=nombre,
                email=correo,
                message=mensaje
            )
            return render(request, 'myfirstapp/contacto.html', {'form': form, 'mensaje': '¡Gracias por contactarnos!'})
    else:
        form = ContactForm()
    
    return render(request, 'myfirstapp/contacto.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        # Pasamos los datos del POST al formulario para validarlos
        form = RegistroForm(request.POST)
        
        if form.is_valid():
            # Si el formulario es válido, limpiamos los datos
            data = form.cleaned_data
            
            # Paso 5 de la imagen: Guardar en la BD
            Usuario.objects.create(
                username=data['username'],
                email=data['email'],
                edad=data['edad'],
                ciudad=data['ciudad']
            )
            
            # Redirigir a una página de éxito o a donde prefieras para evitar reenvíos

    else:
        # Si es GET, creamos el formulario vacío
        form = RegistroForm()
        
    return render(request, 'myfirstapp/registro.html', {'form': form})


def home(request):
    return render(request, 'myfirstapp/home.html')

def nosotros(request):
    return render(request, 'myfirstapp/nosotros.html')

def productos1(request):
    return render(request, 'myfirstapp/productos1.html')

def perfil(request):
    return render(request, 'myfirstapp/perfil.html')

def tareas(request):
    lista_tareas = [
        {'titulo': 'Estudiar Django', 'completada': True},
        {'titulo': 'Hacer ejercicio', 'completada': False},
        {'titulo': 'Leer documentación', 'completada': False},
        {'titulo': 'Practicar templates', 'completada': True},
    ]
    context = {
        'tareas': lista_tareas
    }
    return render(request, 'myfirstapp/tareas.html', context)

def productos2(request):
    return render(request, 'myfirstapp/productos2.html')

def productos3(request):
    return render(request, 'myfirstapp/productos3.html')

def presentacion(request):
    return render(request, 'myfirstapp/presentacion.html')


def contacto(request):
    return render(request, 'myfirstapp/contacto.html')

