from django.contrib import admin
from . import models


@admin.register(models.BankAccountModel)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',
    list_filter = ['id', 'title',]
    search_fields = ['id', 'title',]
    list_editable = ['title',]
    empty_value_display = 'Vazio'
    list_per_page = 20


@admin.register(models.CardModel)
class CardAdmin(admin.ModelAdmin):
    list_display = 'id', 'id_bank_account', 'card_number', 'payment_day',
    list_filter = ['id', 'id_bank_account', 'card_number', 'payment_day',]
    search_fields = ['id', 'id_bank_account', 'card_number', 'payment_day',]
    list_editable = ['id_bank_account',]
    empty_value_display = 'Vazio'
    list_per_page = 20
