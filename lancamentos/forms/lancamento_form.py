
from django import forms
from lancamentos.models import *
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
            # 'description': forms.Textarea,
            # 'valor_total': forms.TextInput
        }

    ...
