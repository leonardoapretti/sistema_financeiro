# from lancamentos.models import Entry, Installment
# from bank_account.models import CardModel
# from django.shortcuts import redirect


# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from datetime import date
# import pandas as pd


# @receiver(post_save, sender=Entry)
# def create_installments(sender, instance, created, *args, **kwargs):
#     if created:
#         entry = instance
#         installs_number = entry.installments_number
#         init_month = ''
#         entry_date = entry.entry_date
#         if str(entry.id_modality) == 'Crédito':
#             card = entry.id_card
#             if card == None:
#                 return redirect('lancamentos:novo')
#             print(card.payment_day)
#             init_month = 1

#         else:
#             init_month = 0

#         install_value = entry.value / installs_number
#         for install_number in range(installs_number):
#             print(entry)
#             install_number += 1
#             due_date = pd.to_datetime(entry_date) + \
#                 pd.DateOffset(months=init_month)
#             data = {
#                 'id_entry': entry,
#                 'installment_number': install_number,
#                 'installment_value': install_value,
#                 'due_date': due_date,
#             }
#             init_month += 1
#             print(data)
#             install = Installment.objects.create(**data)
