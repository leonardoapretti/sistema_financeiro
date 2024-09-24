from typing import Any
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Installment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_entry = models.ForeignKey(
        to='lancamentos.Entry', on_delete=models.CASCADE, verbose_name='Lancamento', blank=True, null=True, default=None, related_name='installments')
    number = models.PositiveIntegerField(
        verbose_name='Numero parcela')
    value = models.FloatField(verbose_name='Valor parcela')
    payment_date = models.DateField(verbose_name='Data de vencimento')
    paid = models.BooleanField(default=False, verbose_name='Paga')
    id_titular_user = models.ForeignKey(
        User, verbose_name='Titular', on_delete=models.CASCADE)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # print(self._meta.fields)
    #     # print(kwargs)
    #     for field in self._meta.fields:
    #         print(field)
    #         # field_object = self._meta.get_field(field)
    #         field_value = field.value_from_object(self)
    #         print(field_value)
    #     # self.initial_value = self.value
    #     # self.initial_payment_date = self.payment_date
    #     # self.initial_paid = self.paid
    #     # self.initial_id_titular_user = self.id_titular_user

    # @classmethod
    # def from_db(cls, db, field_names, values):
    #     instance = super().from_db(db, field_names, values)
    #     instance.initial_value = instance.value
    #     instance.initial_payment_date = instance.payment_date
    #     instance.initial_paid = instance.paid
    #     instance.initial_id_titular_user = instance.id_titular_user
    #     return instance

    def __str__(self):
        return f'{self.id_entry}'

    def get_absolute_url(self):
        return reverse('entries:installment_update', args=(self.id,))
