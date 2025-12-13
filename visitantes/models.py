from django.db import models

class Visitante(models.Model):
    TIPOS_VISITANTE = [
        ('IND', 'Individual'),
        ('GRP', 'Grupo/Escola'),
    ]
    
    
    nome = models.CharField(max_length=150) 
    contato = models.CharField(max_length=100)
    quantidade = models.IntegerField(default=1) 
    tipo = models.CharField(max_length=3, choices=TIPOS_VISITANTE, default='IND')

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

class Visita(models.Model):
   
    data_visita = models.DateTimeField()
    
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)

    def __str__(self):
        return f"Visita em {self.data_visita} - {self.visitante.nome}"