from django.http import HttpResponseRedirect
from django.views.generic import View
from lancamentos.models.payment_model import Payment
from lancamentos.models.installment_model import Installment
from django.shortcuts import redirect
import datetime
from django.contrib import messages


class PayInstallmentView(View):
    def post(self, request, *args, **kwargs):
        installment = Installment.objects.get(id=request.POST['id'] or None)
        if installment == None:
            messages.error(
                self.request, 'Algo deu errado com a sua requisição!')
            return redirect('entries:installment_list')

        if installment.paid:
            installment.paid = False
            messages.info(request, 'Despesa pendente!')
        else:
            installment.paid = True
            messages.success(request, 'Despesa quitada!')

        installment.save()
        return redirect(request.META['HTTP_REFERER'])
