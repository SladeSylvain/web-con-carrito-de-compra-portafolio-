from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tarea

@login_required
def tareas(request):
    if request.method == 'POST':
        # 1. ACCIÓN: AGREGAR TAREA
        if 'agregar' in request.POST:
            titulo = request.POST.get('titulo', '').strip()
            if titulo:
                Tarea.objects.create(titulo=titulo)
                messages.success(request, 'Tarea agregada correctamente.')
        
        # 2. ACCIÓN: ELIMINAR TAREA
        elif 'eliminar' in request.POST:
            tarea_id = request.POST.get('tarea_id')
            Tarea.objects.filter(id=tarea_id).delete()
            messages.warning(request, 'Tarea eliminada.')

        # 3. ACCIÓN: MARCAR COMO COMPLETADA / PENDIENTE (TOGGLE)
        elif 'toggle' in request.POST:
            tarea_id = request.POST.get('tarea_id')
            try:
                tarea = Tarea.objects.get(id=tarea_id)
                tarea.completada = not tarea.completada
                tarea.save()
                estado = 'completada' if tarea.completada else 'pendiente'
                messages.info(request, f'Tarea marcada como {estado}.')
            except Tarea.DoesNotExist:
                pass

        return redirect('tareas')

    context = {
        'tareas': Tarea.objects.all().order_by('-creada')
    }
    return render(request, 'tasks/tareas.html', context)
