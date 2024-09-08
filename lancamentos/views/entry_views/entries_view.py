from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView
from lancamentos.models import Entry
import datetime
from django.db.models import Q


class EntriesView(ListView):
    model = Entry
    context_object_name = 'entries'
    template_name = 'entries/pages/entries.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = ListView.get_queryset(self, *args, **kwargs)
        if self.request.method == 'POST':
            return qs.filter(
                Q(entry_date__gte=self.request.POST['start_date']),
                Q(entry_date__lte=self.request.POST['end_date']),
                Q(id_titular_user=self.request.user.id) | Q(shared=True))
        return qs.filter(Q(id_titular_user=self.request.user.id) | Q(shared=True))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['redirect_filter_url'] = reverse('lancamentos:extrato')
        print(context)
        return context
