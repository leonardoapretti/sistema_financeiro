from django.views.generic import ListView
from bank_account.models import CardModel


class CardListView(ListView):
    template_name = 'bank_account/pages/cards.html'
    model = CardModel
    context_object_name = 'cards'

    def get_queryset(self):
        qs = super().get_queryset()
        f_qs = qs
        return f_qs
