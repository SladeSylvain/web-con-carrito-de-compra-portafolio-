from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm

def registro(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def perfil(request):
    # En el perfil real, los datos provienen del usuario autenticado en la request.
    # Podemos pasar créditos mock o basados en su rol (por ejemplo, $45.200 si es VIP)
    context = {
        'user': request.user,
        'es_vip': request.user.is_staff or request.user.is_superuser or (len(request.user.username) % 2 == 0),
        'creditos': 45200 if (len(request.user.username) % 2 == 0) else 0,
        'pedidos_count': 12 if (len(request.user.username) % 2 == 0) else 0,
    }
    return render(request, 'accounts/perfil.html', context)
