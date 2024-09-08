from django.db import models
from lancamentos.models.entry_model import Entry
from django.contrib.auth.models import User


class Installment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_entry = models.ForeignKey(
        Entry, on_delete=models.CASCADE, verbose_name='Lancamento', blank=True, null=True, default=None, related_name='installments')
    number = models.PositiveIntegerField(
        verbose_name='Numero parcela')
    value = models.FloatField(verbose_name='Valor parcela')
    payment_date = models.DateField(verbose_name='Data de vencimento')
    paid = models.BooleanField(default=False, verbose_name='Paga')
    id_titular_user = models.ForeignKey(
        User, verbose_name='Titular', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id_entry}'
