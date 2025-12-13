from django import forms
from .models import Exposicao

class ExposicaoForm(forms.ModelForm):
    class Meta:
        model = Exposicao
        fields = ['nome', 'descricao', 'data_inicio', 'data_fim']
        
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }