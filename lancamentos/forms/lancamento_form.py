
from django import forms
from lancamentos.models import Lancamento


class LancamentoForm(forms.ModelForm):
    class Meta:
        model = Lancamento
        fields = '__all__'
