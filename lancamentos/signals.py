# from lancamentos.models import Entry

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from datetime import date
# import pandas as pd


# @receiver(post_save, sender=Entry)
# def create_parcelas(sender, instance, created, *args, **kwargs):
#     if created:
#         lancamento = instance
#         qtd_parcelas = lancamento.quantidade_parcelas
#         id_lancamento = lancamento.id
#         valor_parcela = lancamento.valor_total / qtd_parcelas
#         for num_parcela in range(qtd_parcelas):
#             print(lancamento)
#             data_vencimento = ''
#             num_parcela += 1
