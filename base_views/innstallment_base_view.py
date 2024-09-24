from typing import Any
from django.views.generic import ListView
from bank_account.models import CardModel
from django.db.models import Q


class InstallmentBaseView(ListView):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

    def get(self, request, *args, **kwargs):
        self.start_date = request.GET.get('start_date', '')
        self.end_date = request.GET.get('end_date', '')

        if self.start_date == '' or self.end_date == '':
            principal_card = self.get_principal_card()
            self.start_date, self.end_date = principal_card.get_bill_cutoff_dates()

        return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     POST = self.request.POST

    #     self.start_date, self.end_date = POST['start_date'], POST['end_date']
    #     return super().get(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        self.queryset = qs.filter(
            Q(payment_date__gte=self.start_date),
            Q(payment_date__lte=self.end_date),
            Q(id_titular_user=self.request.user.id))
        return self.queryset

    def get_principal_card(self):
        return CardModel.objects.filter(principal=True).first()

    def get_totalizers(self):
        qs = self.queryset

        totalizers = {
            'sum_debits': 0,
            'sum_paid_shared_debits': 0,
            'sum_pending_shared_debits': 0,
            'sum_not_shared_paid_debits': 0,
            'sum_not_shared_pendent_debits': 0,
            'sum_credits': 0,
            'sum_shared_credits': 0,
            'sum_not_shared_credits': 0,
        }

        for install in qs:
            shared = install.id_entry.shared

            if str(install.id_entry.id_type) == 'Despesa':
                totalizers['sum_debits'] += install.value
                if shared:
                    if install.paid == True:
                        totalizers['sum_paid_shared_debits'] += install.value
                        continue
                    totalizers['sum_pending_shared_debits'] += install.value
                else:
                    if install.paid == True:
                        totalizers['sum_not_shared_paid_debits'] += install.value
                        continue
                    totalizers['sum_not_shared_pendent_debits'] += install.value

            elif str(install.id_entry.id_type) == 'Receita':
                totalizers['sum_credits'] += install.value
                if shared:
                    totalizers['sum_shared_credits'] += install.value
                else:
                    totalizers['sum_not_shared_credits'] += install.value

        return totalizers
