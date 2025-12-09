from django.db import models

class Peca(models.Model):
    
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150, blank=True)
    origem = models.CharField(max_length=100, blank=True)
    ano = models.IntegerField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    estado_conservacao = models.CharField(max_length=100)
    
    categoria = models.ForeignKey('categorias.Categoria', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo