from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Denuncia
from .forms import DenunciaForm

def lista_denuncias(request):
    denuncias = Denuncia.objects.all().order_by('-data_criacao')
    return render(request, 'core/lista.html', {'denuncias': denuncias})

def criar_denuncia(request):
    if request.method == 'POST':
        form = DenunciaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_denuncias')
    else:
        form = DenunciaForm()
    return render(request, 'core/form.html', {'form': form})

