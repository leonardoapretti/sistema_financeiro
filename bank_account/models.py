from django.db import models
from django.contrib.auth.models import User


class BankAccountModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_titular_user = models.ForeignKey(
        User, verbose_name='Usuario', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Titulo', max_length=65)

    class Meta:
        verbose_name = 'Bank account'


class CardModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_bank_account = models.ForeignKey(
        BankAccountModel, on_delete=models.CASCADE)
    card_number = models.CharField(
        verbose_name='Numero cartão', max_length=65, blank=True, default=None)
    payment_day = models.IntegerField(verbose_name='Data vencimento')

    class Meta:
        verbose_name = 'Card'
