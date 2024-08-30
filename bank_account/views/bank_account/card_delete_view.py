from django.views.generic import DeleteView
from bank_account.models import CardModel
from django.urls import reverse
from django.contrib import messages


class CardDeleteView(DeleteView):
    model = CardModel

    def get_success_url(self):
        messages.success(self.request, 'Cartão apagado!')
        return reverse('bank_account:cards')
