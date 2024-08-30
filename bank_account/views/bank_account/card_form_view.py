from django.views.generic import FormView
from bank_account.forms.bank_account_form import BankAccountForm


class BankAccountFormView(FormView):
    template_name = 'bank_account/pages/new_account.html'
    form_class = BankAccountForm
    context_object_name = 'form'
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
