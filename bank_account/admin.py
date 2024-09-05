from django.contrib import admin
from . import models


@admin.register(models.BankAccountModel)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'id_titular_user'
    list_filter = ['id', 'title', 'id_titular_user']
    search_fields = ['id', 'title', 'id_titular_user']
    list_editable = ['title', 'id_titular_user']
    empty_value_display = 'Vazio'
    list_per_page = 20


@admin.register(models.CardModel)
class CardAdmin(admin.ModelAdmin):
    list_display = 'id', 'id_bank_account', 'card_name', 'turn_day', 'payment_day', 'principal', 'id_bank_account__id_titular_user',
    list_filter = ['id', 'id_bank_account',
                   'card_name', 'payment_day', 'principal',]
    search_fields = ['id', 'id_bank_account',
                     'card_name', 'payment_day', 'principal',]
    list_editable = ['id_bank_account',
                     'card_name', 'payment_day', 'turn_day', 'principal',]
    empty_value_display = 'Vazio'
    list_per_page = 20

    # adicionando campos extras de classes de foreign keys
    def titular_user(self, obj):
        return obj.id_bank_account.id_titular_user
