
from django import forms
from lancamentos.models import *
from django.contrib.auth.models import User


class LancamentoForm(forms.ModelForm):
    titulo = forms.CharField(
        help_text='Digite uma breve descrição do lançamento',
    )

    class Meta:
        model = Lancamento
        fields = '__all__'
        exclude = ['slug', 'id_usuario_ativo']
        widgets = {
            'id_modalidade': forms.RadioSelect
        }

    ...
