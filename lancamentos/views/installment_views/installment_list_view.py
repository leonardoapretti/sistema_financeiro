from base_views.extract_base_view import ExtractBaseView
from lancamentos.models import Installment


class InstallmentListView(ExtractBaseView):
    model = Installment
    template_name = 'lancamentos/pages/installment_extract.html'
    context_object_name = 'installments'
    ordering = ['-id_entry__entry_date']

    def get(self, request, *args, **kwargs):
        principal_card = self.get_principal_card()
        self.start_date, self.end_date = principal_card.get_cutoff_dates()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(InstallmentListView, self).get_context_data(**kwargs)
        context['totalizers'] = self.get_totalizers()
        return context
