from django.shortcuts import render, redirect, get_object_or_404
from .models import Exposicao
from .forms import ExposicaoForm

def listar_exposicoes(request):
    exposicoes = Exposicao.objects.all()
    return render(request, 'exposicoes/listar_exposicoes.html', {'exposicoes': exposicoes})

def cadastrar_exposicao(request):
    if request.method == 'POST':
        form = ExposicaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_exposicoes')
    else:
        form = ExposicaoForm()
    return render(request, 'exposicoes/form_exposicao.html', {'form': form})

def editar_exposicao(request, id):
    exposicao = get_object_or_404(Exposicao, id=id)
    
    if request.method == 'POST':
        form = ExposicaoForm(request.POST, instance=exposicao)
        if form.is_valid():
            form.save()
            return redirect('listar_exposicoes')
    else:
        form = ExposicaoForm(instance=exposicao)
    
    return render(request, 'exposicoes/form_exposicao.html', {'form': form})

def excluir_exposicao(request, id):
    exposicao = get_object_or_404(Exposicao, id=id)
    
    if request.method == 'POST':
        exposicao.delete()
        return redirect('listar_exposicoes')
    
    return render(request, 'exposicoes/confirmar_exclusao.html', {'exposicao': exposicao})