from django.shortcuts import render, redirect
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