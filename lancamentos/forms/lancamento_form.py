
from django import forms
from lancamentos.models import *
# from django.contrib.auth.models import User


class LancamentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LancamentoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            label = visible.field.label
            match label:
                case 'Modalidade' | 'Tipo' | 'Instituição financeira':
                    visible.field.widget.attrs['class'] = 'custom-select'

                case _:  # default do python
                    visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Lancamento
        fields = '__all__'
        exclude = ['slug', 'id_usuario_ativo']
        widgets = {
            'descricao': forms.Textarea,
        }

    ...
