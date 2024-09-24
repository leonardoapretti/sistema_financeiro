from django.urls import reverse_lazy
from django.views.generic import UpdateView
from lancamentos.forms.entry_form import EntryForm

from lancamentos.models import Entry


class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entries/pages/new.html'

    def get_form_kwargs(self):
        kwargs = super(EntryUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        super().get_success_url()
        return self.get_object().get_absolute_url()
