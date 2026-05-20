from django.shortcuts import render


# Create your views here.

def contacto(request):
    return render(request, 'myfirstapp/contacto.html')

def home(request):
    return render(request, 'myfirstapp/home.html')

def nosotros(request):
    return render(request, 'myfirstapp/nosotros.html')

def productos(request):
    return render(request, 'myfirstapp/productos.html')

