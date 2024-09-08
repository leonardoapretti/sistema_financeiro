from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from lancamentos.forms.entry_form import EntryForm

from lancamentos.models import Entry


class EntryUpdateView(UpdateView):
    model = Entry
    fields = '__all__'
    Form_class = EntryForm
    template_name = 'result/assessmentScore.html'
    success_url = reverse_lazy('lancamentos:home')
