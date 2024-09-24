from django.http import HttpResponseRedirect
from django.views.generic import View
from lancamentos.models.payment_model import Payment
from lancamentos.models.installment_model import Installment
from django.shortcuts import redirect
import datetime
from django.contrib import messages

"""
TODO
para cada pagamento deverá ser lançada uma receita para o usuário que está vinculado como credor da despesa, caso haja
"""


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

        # today = datetime.date.today()
        # payment_data = {
        #     'id_installment': installment,
        #     'date': today,
        #     'value': installment.value,
        #     'id_active_user': request.user,

        # }

        # Payment.objects.create(**payment_data)
        # TODO implementar redirect com filtro
        return redirect(request.META['HTTP_REFERER'])
