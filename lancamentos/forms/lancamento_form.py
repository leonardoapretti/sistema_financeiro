
from django.core.exceptions import ValidationError
from django import forms
from lancamentos.models import *
import datetime
# from django.contrib.auth.models import User


class LancamentoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LancamentoForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            input_type = visible.field.widget.__class__.__name__
            match input_type:
                case 'Select':
                    visible.field.widget.attrs['class'] = 'custom-select'

                case _:
                    visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Entry
        fields = '__all__'
        exclude = ['slug', 'id_active_user']
        widgets = {
            # TODO RETORNAR APÓS DESENVOLVIMENTO
            # 'entry_date': forms.DateInput(attrs={"type": "date"}),
            # 'valor_total': forms.TextInput
        }

    def clean(self):
        cleaned_data = super().clean()
        modality = cleaned_data['id_modality']
        bank = cleaned_data['id_bank_account']
        card = cleaned_data['id_card']
        if str(modality) == 'Crédito' and (bank == None or card == None):
            raise ValidationError(
                'Banco e Cartão não podem estar em branco!', 'invalid')

        return cleaned_data
