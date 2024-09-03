from django.views.generic import FormView
from bank_account.forms.bank_account_form import BankAccountForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class BankAccountFormView(FormView):
    template_name = 'bank_account/pages/new_account.html'
    form_class = BankAccountForm
    context_object_name = 'form'
    success_url = reverse_lazy('bank_account:new_card')

    def form_valid(self, form):
        bank_account = form.save(commit=False)
        bank_account.id_titular_user = self.request.user
        bank_account.save()
        messages.success(
            self.request, 'Banco cadastrado!')
        return super().form_valid(form)
