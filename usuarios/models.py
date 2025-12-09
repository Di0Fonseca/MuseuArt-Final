from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    
    NIVEIS_ACESSO = [
        ('ADM', 'Administrador'),
        ('CUR', 'Curador'),
        ('REC', 'Recepcionista/Guia'),
    ]
    
    nivel_acesso = models.CharField(max_length=3, choices=NIVEIS_ACESSO, default='REC')
    
    nome_completo = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username