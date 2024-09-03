from django.views.generic import FormView
from bank_account.forms.card_form import CardForm
from bank_account.models import CardModel
from django.urls import reverse_lazy
from django.contrib import messages


class CardFormView(FormView):
    template_name = 'bank_account/pages/new_card.html'
    form_class = CardForm
    context_object_name = 'form'
    success_url = reverse_lazy('bank_account:new_card')

    #  passa argumentos para o form
    def get_form_kwargs(self):

        kwargs = super(CardFormView, self).get_form_kwargs()

        kwargs['user'] = self.request.user

        return kwargs

    def form_valid(self, form):
        cards_len = len(CardModel.objects.filter(
            id_bank_account__id_titular_user=self.request.user))

        card = form.save(commit=False)
        if cards_len == 0:
            card.principal = True

        card.save()
        messages.success(self.request, 'Cartão cadastrato!')
        return super().form_valid(card)
