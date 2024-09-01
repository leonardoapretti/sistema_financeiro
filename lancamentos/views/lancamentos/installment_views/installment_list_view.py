from typing import Any
from django.db.models import Q
from django.views.generic import ListView
from lancamentos.models import Installment
import datetime


class InstallmentListView(ListView):
    model = Installment
    template_name = 'lancamentos/pages/installment_extract.html'
    context_object_name = 'installments'
    ordering = ['-id_entry__entry_date']

    def get_cutoff_dates(self, due_date):
        today = datetime.date.today()
        cutoff_dates = {}
        if (today.day < due_date):
            cutoff_dates['start_date'] = datetime.date(
                today.year, today.month - 1, due_date)
            cutoff_dates['end_date'] = datetime.date(
                today.year, today.month, due_date)
        else:
            cutoff_dates['start_date'] = datetime.date(
                today.year, today.month, due_date)
            cutoff_dates['end_date'] = datetime.date(
                today.year, today.month + 1, due_date)
        return cutoff_dates

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        f_qs = qs
        if self.request.method == 'POST' and self.request.POST['start_date'] != '' and self.request.POST['end_date'] != '':
            POST = self.request.POST
            return f_qs.filter(
                Q(due_date__lte=POST['end_date']),
                Q(due_date__gt=POST['start_date']),
                Q(id_entry__id_titular_user=self.request.user.id) | Q(id_entry__shared=True))

        cutoff_dates = self.get_cutoff_dates(
            due_date=f_qs.first().id_entry.id_card.payment_day)

        return f_qs.filter(
            Q(due_date__lte=cutoff_dates['end_date']),
            Q(due_date__gte=cutoff_dates['start_date']),
            Q(id_entry__id_titular_user=self.request.user.id) | Q(id_entry__shared=True))

    def get_context_data(self, **kwargs):
        context = super(InstallmentListView, self).get_context_data(**kwargs)
        context['totalizers'] = self.get_totalizers()
        print(context)
        return context

    def get_totalizers(self):
        qs = self.get_queryset()

        totalizers = {
            'sum_not_shared_debits': 0,
            'sum_shared_debits': 0,
            'sum_debits': 0,
            'sum_credits': 0,
        }

        # TODO continuar totalizadores
        for install in qs:
            shared = install.id_entry.shared
            if shared:
                totalizers['sum_shared_debits'] += install.value
            else:
                totalizers['sum_not_shared_debits'] += install.value

            if str(install.id_entry.id_type) == 'Despesa':
                totalizers['sum_debits'] += install.value
            elif str(install.id_entry.id_type) == 'Receita':
                totalizers['sum_credits'] += install.value

        return totalizers
