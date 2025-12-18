from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria
from .forms import CategoriaForm

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar_categorias.html', {'categorias': categorias})

def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/form_categoria.html', {'form': form})

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'categorias/form_categoria.html', {'form': form})

def excluir_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    
    if request.method == 'POST':
        categoria.delete()
        return redirect('listar_categorias')
    
    return render(request, 'categorias/confirmar_exclusao.html', {'categoria': categoria})