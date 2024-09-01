# # from django.urls import reverse
# # from django.utils.crypto import get_random_string
# # from django.utils.text import slugify
# # from django.db import models
# # from django.contrib.auth.models import User
# # from datetime import date
# # from bank_account.models import CardModel, BankAccountModel


# # class Category(models.Model):
# #     id = models.AutoField(primary_key=True, editable=False)
# #     title = models.CharField(max_length=65)

# #     def __str__(self):
# #         return self.title

# #     class Meta:
# #         ordering = ['title']


# # class Type(models.Model):
# #     id = models.AutoField(primary_key=True, editable=False)
# #     title = models.CharField(max_length=65)

# #     def __str__(self) -> str:
# #         return self.title

# #     class Meta:
# #         ordering = ['title']


# # class Modality(models.Model):
# #     id = models.AutoField(primary_key=True, editable=False)
# #     title = models.CharField(max_length=65)

# #     def __str__(self):
# #         return self.title

# #     class Meta:
# #         ordering = ['title']


# class Installment(models.Model):
#     id = models.AutoField(primary_key=True, editable=False)
#     id_entry = models.ForeignKey(
#         Entry, on_delete=models.CASCADE, verbose_name='Lancamento')
#     number = models.PositiveIntegerField(
#         verbose_name='Numero parcela')
#     value = models.FloatField(verbose_name='Valor parcela')
#     due_date = models.DateField(verbose_name='Data de vencimento')


# class Payments(models.Model):
#     id = models.AutoField(primary_key=True, editable=False)
#     id_installment = models.ForeignKey(Entry, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     value = models.FloatField()

#     class Meta:
#         verbose_name = 'Lançamento Baixa'
#         verbose_name_plural = 'Lançamentos Baixas'

#     def __str__(self):
#         return self.id
