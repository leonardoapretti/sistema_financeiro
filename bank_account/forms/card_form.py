from django import forms
from bank_account.models import *


class CardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CardForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            input_type = visible.field.widget.__class__.__name__
            match input_type:
                case 'Select':
                    visible.field.widget.attrs['class'] = 'custom-select'

                case _:
                    visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CardModel
        fields = '__all__'
