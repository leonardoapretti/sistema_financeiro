from django.views.generic import DeleteView
from bank_account.models import BankAccountModel
from django.urls import reverse
from django.contrib import messages


class BankDeleteView(DeleteView):
    model = BankAccountModel

    def get_success_url(self):
        messages.success(self.request, 'Banco apagado!')
        return reverse('bank_account:banks')
