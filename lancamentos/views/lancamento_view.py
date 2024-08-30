from django.views.generic import DetailView
from lancamentos.models import Entry
from django.contrib import messages
from django.shortcuts import redirect, render


class LancamentoView(DetailView):
    model = Entry
    template_name = 'lancamentos/pages/lancamento.html'
    context_object_name = 'lancamento'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)

        return contexto
