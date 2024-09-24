from django import forms
from lancamentos.models.installment_model import Installment


class InstallmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InstallmentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            input_type = visible.field.widget.__class__.__name__
            match input_type:
                case 'Select':
                    visible.field.widget.attrs['class'] = 'custom-select'

                case _:
                    visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Installment
        fields = ('value', 'payment_date', 'paid', 'id_titular_user',)
