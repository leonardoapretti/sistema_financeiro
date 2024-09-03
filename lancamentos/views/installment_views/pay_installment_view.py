from django.views import View
from lancamentos.models.payment_model import Payment
from lancamentos.models.installment_model import Installment
from django.shortcuts import redirect
import datetime
from django.contrib import messages


class PayInstallmentView(View):
    def redirect(self):
        return redirect('lancamentos:installment_list')

    def post(self, request, *args, **kwargs):
        installment = Installment.objects.get(id=request.POST['id'] or None)
        if installment == None:
            messages.error(
                self.request, 'Algo deu errado com a sua requisição!')
            return redirect('lancamentos:installment_pay')
        print(installment)
        today = datetime.date.today()
        payment_data = {
            'id_installment': installment,
            'date': today,
            'value': installment.value,
            'id_active_user': request.user,

        }
        Payment.objects.create(**payment_data)
        messages.success(request, 'Despesa quitada!')
        return redirect('lancamentos:installment_pay')
