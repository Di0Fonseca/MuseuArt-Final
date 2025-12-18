from django.shortcuts import render, redirect, get_object_or_404
from .models import Restauracao
from .forms import RestauracaoForm

def listar_restauracoes(request):
    restauracoes = Restauracao.objects.all()
    return render(request, 'restauracoes/listar_restauracoes.html', {'restauracoes': restauracoes})

def registrar_restauracao(request):
    if request.method == 'POST':
        form = RestauracaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_restauracoes')
    else:
        form = RestauracaoForm()
    return render(request, 'restauracoes/form_restauracao.html', {'form': form})

def editar_restauracao(request, id):
    restauracao = get_object_or_404(Restauracao, id=id)
    
    if request.method == 'POST':
        form = RestauracaoForm(request.POST, instance=restauracao)
        if form.is_valid():
            form.save()
            return redirect('listar_restauracoes')
    else:
        form = RestauracaoForm(instance=restauracao)
    
    return render(request, 'restauracoes/form_restauracao.html', {'form': form})

def excluir_restauracao(request, id):
    restauracao = get_object_or_404(Restauracao, id=id)
    
    if request.method == 'POST':
        restauracao.delete()
        return redirect('listar_restauracoes')
    
    return render(request, 'restauracoes/confirmar_exclusao.html', {'restauracao': restauracao})