from django.contrib import messages
from django.urls import reverse
from django.views.generic.edit import DeleteView
from lancamentos.models import Entry


class DeleteLancamentoView(DeleteView):
    model = Entry

    def get_success_url(self):
        messages.success(self.request, 'Lançamento apagado!')
        return reverse('lancamentos:extrato')
