from django.db import models
from django.contrib.auth.models import User
from datetime import date
from lancamentos.models import Entry


class Payment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_installment = models.ForeignKey(Entry, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()

    class Meta:
        verbose_name = 'Lançamento Baixa'
        verbose_name_plural = 'Lançamentos Baixas'

    def __str__(self):
        return self.id
