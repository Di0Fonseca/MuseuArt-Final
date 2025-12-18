from django import forms
from .models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ['nome', 'contato', 'quantidade', 'tipo']
        
        labels = {
            'contato': 'Observação / Contato',
            'nome': 'Nome do Visitante',
        }

        widgets = {
            'contato': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }