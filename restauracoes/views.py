from django.shortcuts import render, redirect
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