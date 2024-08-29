from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView
from lancamentos.models import Lancamento
import datetime
from django.db.models import Q


class ExtratoView(ListView):
    model = Lancamento
    # paginate_by = 2
    context_object_name = 'lancamentos'
    template_name = 'lancamentos/pages/extrato.html'

    def get_cutoff_dates(self):
        hoje = datetime.date.today()
        dia_corte = 31
        cutoff_dates = {}
        if (hoje.day < dia_corte):
            cutoff_dates['start_date'] = datetime.date(
                hoje.year, hoje.month - 1, dia_corte)
            cutoff_dates['end_date'] = datetime.date(
                hoje.year, hoje.month, dia_corte - 1)
        else:
            cutoff_dates['start_date'] = datetime.date(
                hoje.year, hoje.month, dia_corte)
            cutoff_dates['end_date'] = datetime.date(
                hoje.year, hoje.month + 1, dia_corte - 1)
        return cutoff_dates

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if self.request.method == 'POST' and self.request.POST['start_date'] != '' and self.request.POST['end_date'] != '':
            POST = self.request.POST
            filtered_qs = qs.filter(
                Q(data_lancamento__lte=POST['end_date']),
                Q(data_lancamento__gte=POST['start_date']),
                Q(id_usuario_titular=self.request.user.id) | Q(compartilhado=True))
            return filtered_qs

        cutoff_dates = self.get_cutoff_dates()

        filtered_qs = qs.filter(
            Q(data_lancamento__lte=cutoff_dates['end_date']),
            Q(data_lancamento__gte=cutoff_dates['start_date']),
            Q(id_usuario_titular=self.request.user.id) | Q(compartilhado=True))
        return filtered_qs
