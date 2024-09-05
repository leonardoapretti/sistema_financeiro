from django.db import models
from django.contrib.auth.models import User
import datetime
from dateutil.relativedelta import relativedelta


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
        BankAccountModel, on_delete=models.CASCADE, verbose_name='Banco', related_name='cartoes', default=None, null=True)
    card_name = models.CharField(
        verbose_name='Nome do cartão', max_length=65)
    payment_day = models.IntegerField(verbose_name='Dia vencimento', default=5)
    turn_day = models.IntegerField(verbose_name='Dia que vira', default=30)
    principal = models.BooleanField(default=False)

    def __str__(self):
        return self.card_name

    class Meta:
        verbose_name = 'Card'

    def get_cutoff_dates(self):
        today = datetime.date.today()
        payment_date = datetime.date(
            today.year, today.month, self.payment_day)
        if today > payment_date:
            payment_date = payment_date + relativedelta(months=1)
        start_date = datetime.date(today.year, today.month, self.turn_day)
        if today < start_date:
            start_date -= relativedelta(months=1)
        if today.day <= payment_date.day:
            start_date -= relativedelta(months=1)
        end_date = start_date + relativedelta(months=1) - relativedelta(days=1)
        return start_date, end_date
