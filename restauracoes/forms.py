from django import forms
from .models import Restauracao

class RestauracaoForm(forms.ModelForm):
    class Meta:
        model = Restauracao
        # Verifique se os nomes batem com seu models.py (ex: 'peca' ou 'id_peca')
        fields = ['peca', 'data_inicio', 'data_fim', 'responsavel', 'descricao']
        
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }