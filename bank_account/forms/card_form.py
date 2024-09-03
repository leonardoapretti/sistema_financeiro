from django import forms
from bank_account.models import *
from django.forms import ValidationError


class CardForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            input_type = visible.field.widget.__class__.__name__
            match input_type:
                case 'Select':
                    visible.field.widget.attrs['class'] = 'custom-select'

                # case 'CheckboxInput':
                #     visible.field.widget.attrs['class'] = 'form-check-input'
                #     print(visible.field.widget.attrs['class'])

                case _:
                    visible.field.widget.attrs['class'] = 'form-control'

        # recupera o usuário passado como parâmetro na view e recupera apenas os bancos que o usuário cadastrou
        self.user = user
        self.fields['id_bank_account'].queryset = BankAccountModel.objects.filter(
            id_titular_user=self.user)

    class Meta:
        model = CardModel
        fields = '__all__'

    def clean_id_bank_account(self):
        cleaned_bank_account = self.cleaned_data['id_bank_account']
        if cleaned_bank_account == None:
            raise ValidationError('O banco não pode ser vazio.', 'invalid')

        return cleaned_bank_account
