from django.db import models

class Restauracao(models.Model):
   
    responsavel = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    descricao = models.TextField()
    
    peca = models.ForeignKey('acervo.Peca', on_delete=models.CASCADE)

    def __str__(self):
        return f"Restauração de {self.peca} ({self.data_inicio})"