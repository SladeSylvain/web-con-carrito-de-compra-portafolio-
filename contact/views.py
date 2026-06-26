from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Contacto
from .forms import ContactForm

@login_required
def contacto(request):
    # Solo los administradores o staff pueden ver los mensajes de contacto
    contactos = Contacto.objects.all().order_by('-created_at') if request.user.is_staff else None
    mensaje_exito = None
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por contactarnos! Tu mensaje ha sido enviado.')
            return redirect('contacto')
    else:
        form = ContactForm()
        
    context = {
        'form': form,
        'contactos': contactos,
    }
    return render(request, 'contact/contacto.html', context)

@login_required
@require_POST
def borrar_contacto(request, pk):
    # Solo los administradores o staff pueden borrar mensajes de contacto
    if not request.user.is_staff:
        raise PermissionDenied
        
    contacto_eliminar = get_object_or_404(Contacto, pk=pk)
    contacto_eliminar.delete()
    messages.warning(request, 'Mensaje de contacto eliminado correctamente.')
    return redirect('contacto')
