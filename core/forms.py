from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['rua', 'bairro', 'referencia', 'descricao', 'foto']
        widgets = {
            'rua': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Av. Beira Mar'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Centro'}),
            'referencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Próximo à padaria'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva a situação'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
        }