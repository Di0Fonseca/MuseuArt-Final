from django.shortcuts import render, redirect
from .models import Peca
from .forms import PecaForm

def listar_pecas(request):
    pecas = Peca.objects.all() 
    return render(request, 'acervo/listar_pecas.html', {'pecas': pecas})

def cadastrar_peca(request):
    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('listar_pecas') 
    else:
        form = PecaForm() 

    return render(request, 'acervo/form_peca.html', {'form': form})
