
from django import forms
from lancamentos.models import Lancamento
from django.contrib.auth.models import User


class LancamentoForm(forms.ModelForm):
    def getUsuarios(self):
        usuarios = User.objects.all()
        print(usuarios)

    class Meta:
        model = Lancamento
        fields = '__all__'
        exclude = ['slug', 'id_usuario_ativo']

    ...
