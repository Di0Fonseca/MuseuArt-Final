from django.shortcuts import render, redirect, get_object_or_404
from .models import Peca
from .forms import PecaForm

from visitantes.models import Visitante
from exposicoes.models import Exposicao
from restauracoes.models import Restauracao

def index(request):
    total_pecas = Peca.objects.count()
    total_visitantes = Visitante.objects.count()
    total_exposicoes = Exposicao.objects.count()
    pecas_restauracao = Restauracao.objects.filter(data_fim__isnull=True).count()
    
 
    pecas = Peca.objects.all()

    context = {
        'total_pecas': total_pecas,
        'total_visitantes': total_visitantes,
        'total_exposicoes': total_exposicoes,
        'pecas_restauracao': pecas_restauracao,
        'pecas': pecas,
    }
    return render(request, 'index.html', context)

def listar_pecas(request):
    pecas = Peca.objects.all() 
    return render(request, 'acervo/listar_pecas.html', {'pecas': pecas})

def cadastrar_peca(request):
    if request.method == 'POST':
        form = PecaForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save() 
            return redirect('home')
    else:
        form = PecaForm() 

    return render(request, 'acervo/form_peca.html', {'form': form})

# --- EDITAR E EXCLUIR ---

def editar_peca(request, id):
    peca = get_object_or_404(Peca, id=id)
    
    if request.method == 'POST':
        form = PecaForm(request.POST, request.FILES, instance=peca)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PecaForm(instance=peca)
    
    return render(request, 'acervo/form_peca.html', {'form': form})

def excluir_peca(request, id):
    peca = get_object_or_404(Peca, id=id)
    
    if request.method == 'POST':
        peca.delete()
        return redirect('home')
    
    return render(request, 'acervo/confirmar_exclusao.html', {'peca': peca})