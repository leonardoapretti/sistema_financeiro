from django.db import models
from django.contrib.auth.models import User
from lancamentos.models.installment_model import Installment


class Payment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_installment = models.ForeignKey(
        Installment, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
    id_active_user = models.ForeignKey(
        User, verbose_name='Usuário', on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        verbose_name = 'Payment'

    def __str__(self):
        return f'{self.id} - {self.id_installment}'
