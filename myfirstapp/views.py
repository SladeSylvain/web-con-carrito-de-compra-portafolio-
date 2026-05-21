from django.shortcuts import render


# Create your views here.

def contacto(request):
    return render(request, 'myfirstapp/contacto.html')

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