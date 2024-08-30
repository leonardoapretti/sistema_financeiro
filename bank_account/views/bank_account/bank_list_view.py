from django.views.generic import ListView
from bank_account.models import BankAccountModel


class BankListView(ListView):
    template_name = 'bank_account/pages/banks.html'
    model = BankAccountModel
    context_object_name = 'banks'

    def get_queryset(self):
        qs = super().get_queryset()
        f_qs = qs
        f_qs = BankAccountModel.objects.filter(
            id_titular_user=self.request.user)
        return f_qs
