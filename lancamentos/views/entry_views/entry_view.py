from django.views.generic import DetailView
from lancamentos.models import Entry
from django.db.models import Sum


class EntryView(DetailView):
    model = Entry
    template_name = 'entries/pages/entry.html'
    context_object_name = 'entry'

    #  passa parametros para o form
    def get_form_kwargs(self):
        kwargs = super(EntryView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entry = context['entry']
        print(entry.get_installments_total_value())
        all_installments_value = entry.get_installments_total_value()

        if all_installments_value != entry.value:
            entry.difference = all_installments_value - entry.value

        return context
