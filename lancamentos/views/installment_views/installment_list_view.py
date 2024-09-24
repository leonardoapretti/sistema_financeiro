from django.urls import reverse
from base_views.innstallment_base_view import InstallmentBaseView
from lancamentos.models import Installment


class InstallmentListView(InstallmentBaseView):
    model = Installment
    template_name = 'entries/pages/installment_extract.html'
    context_object_name = 'installments'
    ordering = ['-id_entry__entry_date']

    def get_context_data(self, **kwargs):
        context = super(InstallmentListView, self).get_context_data(**kwargs)
        context['totalizers'] = self.get_totalizers()
        context['redirect_filter_url'] = reverse(
            'entries:installment_list')
        return context
