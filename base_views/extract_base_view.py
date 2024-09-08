from django.views.generic import ListView
from bank_account.models import CardModel
from django.db.models import Q


class ExtractBaseView(ListView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def post(self, request, *args, **kwargs):
        POST = self.request.POST

        self.start_date, self.end_date = POST['start_date'], POST['end_date']
        return super().get(request, *args, **kwargs)

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
            'sum_shared_debits': 0,
            'sum_not_shared_debits': 0,
            'sum_credits': 0,
            'sum_shared_credits': 0,
            'sum_not_shared_credits': 0,
        }

        for install in qs:
            shared = install.id_entry.shared

            if str(install.id_entry.id_type) == 'Despesa':
                totalizers['sum_debits'] += install.value
                if shared:
                    totalizers['sum_shared_debits'] += install.value
                else:
                    totalizers['sum_not_shared_debits'] += install.value

            elif str(install.id_entry.id_type) == 'Receita':
                totalizers['sum_credits'] += install.value
                if shared:
                    totalizers['sum_shared_credits'] += install.value
                else:
                    totalizers['sum_not_shared_credits'] += install.value

        return totalizers
