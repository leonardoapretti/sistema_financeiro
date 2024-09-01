from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from lancamentos.forms import LancamentoForm
from lancamentos.models import Entry
import datetime
# finalizar essa alteração


class NewEntryView(FormView):
    template_name = 'lancamentos/pages/novo.html'
    context_object_name = 'form'
    success_url = reverse_lazy('lancamentos:novo')
    form_class = LancamentoForm

    # from ContextMixin via FormMixin

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

    # def create_installments(self)
