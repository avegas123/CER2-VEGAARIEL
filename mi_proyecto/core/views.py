from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm

# Create your views here.

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada con exito para {username}!')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'core/registrar.html', {'form': form})

def acerca_de(request):
    return render(request, 'core/acerca_de.html')

@login_required
def perfil(request):
    return render(request, 'core/perfil.html')