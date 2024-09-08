from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from lancamentos.forms import EntryForm
import datetime
from bank_account.models import BankAccountModel
# finalizar essa alteração


class NewEntryView(FormView):
    template_name = 'entries/pages/new.html'
    context_object_name = 'form'
    success_url = reverse_lazy('lancamentos:novo')
    form_class = EntryForm

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(NewEntryView, self).get_form_kwargs()
        # kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        data = super(NewEntryView, self).get_context_data(**kwargs)

        form = data['form']
        # TODO implementar posteriormente
        initial = {
            'id_category': form['id_category'][1],
            'title': 'titulo',
            # 'entry_date': datetime.date.today(),
            'value': 20,
            'id_titular_user': self.request.user,
            'id_bank_account': form['id_bank_account'][1]
        }
        form.initial = initial

        form.user = self.request.user
        return data

    def form_valid(self, form):
        entry = form.save(commit=False)
        entry.id_active_user = self.request.user
        entry.save()
        # messages.success(
        #     self.request, f'{entry.id_type} cadastrada!')
        return redirect('lancamentos:create_installment', entry_id=entry.id)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'Algo deu errado com a sua requisição!')
        return response
