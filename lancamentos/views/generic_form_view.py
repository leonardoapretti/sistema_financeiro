from typing import Any
from django.views.generic import FormView
from lancamentos.forms.generic_form import GenericForm


class GenericFormView(FormView):
    template_name = 'lancamentos/partials/generic_form.html'
    form_class = GenericForm

    # def __init__(self, *args, **kwargs):
    #     for field in self.fields:
    #         print(field)
    #     super().__init__(*args, **kwargs)

    # formatar os inputs e labels - verificar possibilidade de implemetar uma FormBaseView para configurar os inputs conforme bootstrap
    def form_valid(self, form):

        return super().form_valid(form)
