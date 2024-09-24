from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from lancamentos.models.installment_model import Installment
from lancamentos.forms.installment_form import InstallmentForm

from django.contrib import messages


class InstallmentUpdateView(UpdateView):
    model = Installment
    form_class = InstallmentForm
    template_name = 'entries/pages/installment_update.html'

    def get_success_url(self):
        super().get_success_url()
        entry = self.get_object().id_entry
        return entry.get_absolute_url()

    def form_valid(self, form):
        installment = form.save(commit=False)
        if installment.value == 0:
            installment.paid = True

        installment.save()
        return super().form_valid(form)

    # def form_invalid(self, form):
    #     response = super().form_invalid(form)
    #     print(response)
    #     return response
