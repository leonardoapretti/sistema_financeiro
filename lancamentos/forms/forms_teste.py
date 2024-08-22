from django import forms
from lancamentos.models import *


class FormTeste(forms.Form):
    nome = forms.CharField(label='Nome', max_length=20, required=False)
    radios = forms.ChoiceField(
        widget=forms.RadioSelect, choices=((1, 'teste1'), (2, 'teste2')))  # assim funciona
