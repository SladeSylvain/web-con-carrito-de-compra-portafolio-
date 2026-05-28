from django.shortcuts import render, redirect
from .forms import ContactForm, RegistroForm
from .models import Contacto, Usuario, Tarea
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


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

@login_required 
def contacto(request):
    contactos = Contacto.objects.all()
    mensaje = None
    
    if request.method == 'POST':
        if request.user.has_perm('myfirstapp.add_contacto'):
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()  
                form = ContactForm()
                mensaje = '¡Gracias por contactarnos!'
        else:
            raise PermissionDenied 
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'contactos': contactos,
        'mensaje': mensaje
    }
    
    return render(request, 'myfirstapp/contacto.html', context)

@login_required
def borrar_contacto(request, pk):
    if not request.user.has_perm('myfirstapp.delete_contacto') and not request.user.has_perm('myfirstapp.add_contacto'):
        raise PermissionDenied
        
    contacto_eliminar = get_object_or_404(Contacto, pk=pk)
    contacto_eliminar.delete()
    messages.warning(request, 'Mensaje eliminado correctamente.')
    return redirect('contacto')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # 1. Pausamos el guardado automático usando commit=False
            # Esto crea el objeto 'usuario' en memoria pero NO lo mete aún a la base de datos
            usuario = form.save(commit=False)
            
            # 2. Rescatamos la contraseña limpia y validada del formulario
            password_plano = form.cleaned_data.get('password')
            
            # 3. Encriptamos la contraseña y se la asignamos al campo del modelo
            usuario.password = make_password(password_plano)
            
            # 4. Ahora que la contraseña es segura, guardamos definitivamente en la BD
            usuario.save()
            
            return render(request, 'myfirstapp/registro.html', {
                'form': RegistroForm(),  # Entregamos un formulario limpio para el próximo registro
                'mensaje': '¡Usuario registrado correctamente y de forma segura!'
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
