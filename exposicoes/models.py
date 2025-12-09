from django.db import models

class Exposicao(models.Model):
    
    nome = models.CharField(max_length=200)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    
    pecas = models.ManyToManyField('acervo.Peca', related_name='exposicoes')

    def __str__(self):
        return self.nome