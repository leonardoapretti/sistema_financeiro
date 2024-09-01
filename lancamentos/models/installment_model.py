from django.db import models
from lancamentos.models.entry_model import Entry
from lancamentos.models.payment_model import Payment


class Installment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_entry = models.ForeignKey(
        Entry, on_delete=models.CASCADE, verbose_name='Lancamento')
    number = models.PositiveIntegerField(
        verbose_name='Numero parcela')
    value = models.FloatField(verbose_name='Valor parcela')
    due_date = models.DateField(verbose_name='Data de vencimento')
    id_payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, verbose_name='Pagamento')
