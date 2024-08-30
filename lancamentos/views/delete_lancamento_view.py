from django.contrib import messages
from django.urls import reverse
from django.views.generic.edit import DeleteView
from lancamentos.models import Lancamento


class DeleteLancamentoView(DeleteView):
    model = Lancamento

    def get_success_url(self):
        messages.success(self.request, 'Lançamento apagado com sucesso!')
        return reverse('lancamentos:extrato')
