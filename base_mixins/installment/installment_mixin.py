from lancamentos.models import Installment

import datetime
from django.contrib import messages
from django.shortcuts import redirect
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User


class InstallmentMixin:
    def create_installment(self):
        payment_date = self.entry.id_card.get_payment_date(
        ) if self.entry.id_modality.title == 'Crédito' else self.entry.entry_date

        installment_value = self.entry.value / self.entry.installments_number

        if self.entry.shared:
            installment_value = installment_value / 2

        installments_number = self.entry.installments_number

        for installment_number in range(installments_number):
            Installment.objects.create(
                id_entry=self.entry,
                number=installment_number + 1,
                value=installment_value,
                payment_date=payment_date +
                relativedelta(months=installment_number),
                id_titular_user=self.request.user
            )

            if self.entry.shared:
                id_titular_user = User.objects.all().exclude(
                    id=self.entry.id_titular_user.id).first()
                Installment.objects.create(
                    id_entry=self.entry,
                    number=installment_number + 1,
                    value=installment_value,
                    payment_date=payment_date +
                    relativedelta(months=installment_number),
                    id_titular_user=id_titular_user
                )
