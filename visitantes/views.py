from django.shortcuts import render, redirect
from .models import Visitante
from .forms import VisitanteForm

def listar_visitantes(request):
    visitantes = Visitante.objects.all()
    return render(request, 'visitantes/listar_visitantes.html', {'visitantes': visitantes})

def registrar_visitante(request):
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_visitantes')
    else:
        form = VisitanteForm()
    return render(request, 'visitantes/form_visitante.html', {'form': form})