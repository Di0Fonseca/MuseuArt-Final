from django import forms
from .models import Peca

class PecaForm(forms.ModelForm):
    class Meta:
        model = Peca
        fields = ['titulo', 'autor', 'origem', 'ano', 'estado_conservacao', 'categoria', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'ano': forms.NumberInput(attrs={'min': 0}),
        }