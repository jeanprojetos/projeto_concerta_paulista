from django import forms
from .models import Denuncia


class DenunciaForm(forms.ModelForm):
    website = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            'class': 'cp-hp',
            'tabindex': '-1',
            'autocomplete': 'off',
        })
    )

    class Meta:
        model = Denuncia
        fields = [
            'categoria', 'rua', 'bairro', 'referencia', 'descricao',
            'foto', 'email_contato', 'latitude', 'longitude',
        ]
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'rua': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Av. Beira Mar'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Centro'}),
            'referencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Próximo à padaria'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva a situação'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'email_contato': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seuemail@exemplo.com'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
