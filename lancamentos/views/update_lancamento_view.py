from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import UpdateView
from lancamentos.forms.lancamento_form import LancamentoForm

from lancamentos.models import Lancamento


class UpdateLancamentoView(UpdateView):
    template_name = 'lancamentos/pages/lancamento.html'
    model = Lancamento
    form_class = LancamentoForm
