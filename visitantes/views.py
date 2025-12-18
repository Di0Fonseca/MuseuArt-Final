from django.shortcuts import render, redirect, get_object_or_404
from .models import Visitante
from .forms import VisitanteForm

def listar_visitantes(request):
    visitantes = Visitante.objects.all().order_by('-visita')
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

def editar_visitante(request, id):
    visitante = get_object_or_404(Visitante, id=id)
    
    if request.method == 'POST':
        form = VisitanteForm(request.POST, instance=visitante)
        if form.is_valid():
            form.save()
            return redirect('listar_visitantes')
    else:
        form = VisitanteForm(instance=visitante)
    
    return render(request, 'visitantes/form_visitante.html', {'form': form})

def excluir_visitante(request, id):
    visitante = get_object_or_404(Visitante, id=id)
    
    if request.method == 'POST':
        visitante.delete()
        return redirect('listar_visitantes')
    
    return render(request, 'visitantes/confirmar_exclusao.html', {'visitante': visitante})