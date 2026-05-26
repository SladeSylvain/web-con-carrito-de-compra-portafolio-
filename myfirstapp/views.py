from django.shortcuts import render, redirect
from .forms import ContactForm, RegistroForm
from .models import Contacto, Usuario, Tarea

# Create your views here.

def home(request):
    return render(request, 'myfirstapp/home.html')

def nosotros(request):
    return render(request, 'myfirstapp/nosotros.html')

def presentacion(request):
    return render(request, 'myfirstapp/presentacion.html')

def perfil(request):
    return render(request, 'myfirstapp/perfil.html')


# --- SECCIÓN PRODUCTOS ---

def productos1(request):
    return render(request, 'myfirstapp/productos1.html')

def productos2(request):
    return render(request, 'myfirstapp/productos2.html')

def productos3(request):
    return render(request, 'myfirstapp/productos3.html')


# --- VISTAS CON FORMULARIOS Y PROCESAMIENTO ---

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos directamente en la BD
            # Retornamos el template con un formulario limpio y el mensaje de éxito
            return render(request, 'myfirstapp/contacto.html', {
                'form': ContactForm(), 
                'mensaje': '¡Gracias por contactarnos!'
            })
    else:
        form = ContactForm()
    
    return render(request, 'myfirstapp/contacto.html', {'form': form})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el nuevo usuario en la BD de forma limpia
            # Retornamos el template con el formulario vacío y el mensaje de éxito
            return render(request, 'myfirstapp/registro.html', {
                'form': RegistroForm(),  
                'mensaje': '¡Usuario registrado correctamente!'
            })
    else:
        form = RegistroForm()
        
    return render(request, 'myfirstapp/registro.html', {'form': form})


def tareas(request):
    if request.method == 'POST':
        # 1. ACCIÓN: AGREGAR TAREA
        if 'agregar' in request.POST:
            titulo = request.POST.get('titulo', '').strip()
            if titulo:
                Tarea.objects.create(titulo=titulo)
        
        # 2. ACCIÓN: ELIMINAR TAREA
        elif 'eliminar' in request.POST:
            tarea_id = request.POST.get('tarea_id')
            Tarea.objects.filter(id=tarea_id).delete()

        # 3. ACCIÓN: MARCAR COMO COMPLETADA / PENDIENTE (TOGGLE)
        elif 'toggle' in request.POST:
            tarea_id = request.POST.get('tarea_id')
            try:
                tarea = Tarea.objects.get(id=tarea_id)
                tarea.completada = not tarea.completada
                tarea.save()
            except Tarea.DoesNotExist:
                pass  # Evita que la app se caiga si la tarea ya no existe

        # Redirecciona a la misma página para limpiar el envío del formulario
        return redirect('tareas')

    # Si es una petición GET (cargar la página por primera vez)
    context = {'tareas': Tarea.objects.all().order_by('-creada')}
    return render(request, 'myfirstapp/tareas.html', context)