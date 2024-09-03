from django.views.generic import View
from lancamentos.models import Installment, Entry
from django.shortcuts import redirect
from django.contrib import messages
import datetime
import pandas as pd


class InstallmentCreateView(View):
    def get(self, request, entry_id):
        entry = Entry.objects.filter(id=entry_id).first()
        installs_number = entry.installments_number
        init_month = ''
        entry_date = entry.entry_date
        today = datetime.date.today()
        print(today)
        if str(entry.id_modality) == 'Crédito':
            card = entry.id_card
            if card == None:
                messages.error(
                    request, 'Selecione um cartão.')
                Entry.objects.filter(id=entry_id).first().delete()
                return redirect('lancamentos:novo')

            entry_date = today
            entry_date = entry_date.replace(
                year=today.year, month=today.month, day=card.payment_day)

            if today.day > card.turn_day:
                init_month = 2
            else:
                init_month = 1

        else:
            init_month = 0

        install_value = entry.value / installs_number

        if entry.shared == True:
            install_value = install_value / 2

        for install_number in range(installs_number):
            install_number += 1
            due_date = pd.to_datetime(entry_date) + \
                pd.DateOffset(months=init_month)
            data = {
                'id_entry': entry,
                'number': install_number,
                'value': install_value,
                'due_date': due_date,
            }
            init_month += 1
            print(data)
            print(Installment.objects.create(**data))
        messages.success(request, f'{entry.id_type} cadastrada!')
        return redirect('lancamentos:novo')
