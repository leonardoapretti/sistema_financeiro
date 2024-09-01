from django.db import models
from django.contrib.auth.models import User


class BankAccountModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_titular_user = models.ForeignKey(
        User, verbose_name='Usuario', on_delete=models.CASCADE, default='')
    title = models.CharField(verbose_name='Titulo', max_length=65)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Bank account'


class CardModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_bank_account = models.ForeignKey(
        BankAccountModel, on_delete=models.CASCADE, verbose_name='Banco', related_name='cartoes', default=None, null=True, blank=True,)
    card_number = models.CharField(
        verbose_name='Numero cartão', max_length=65, blank=True, default=None)
    payment_day = models.IntegerField(verbose_name='Dia vencimento', default=5)
    turn_day = models.IntegerField(verbose_name='Dia que vira', default=30)

    def __str__(self):
        return self.card_number

    class Meta:
        verbose_name = 'Card'
