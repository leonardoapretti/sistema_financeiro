from django.views.generic import FormView
from bank_account.forms.card_form import CardForm
from django.urls import reverse_lazy


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
        form.save()
        return super().form_valid(form)
