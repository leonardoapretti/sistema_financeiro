from django.contrib import admin
from lancamentos import models


@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = 'id', 'entry_date', 'title',  'description', 'installments_number',  'value', 'id_category',  'id_modality', 'id_type', 'shared', 'fixed', 'id_titular_user', 'id_active_user', 'slug', 'id_card', 'id_bank_account',
    # list_filter = ['entry_date', 'shared',
    #                'installments_number', 'description', 'id_category', 'id_modality']
    search_fields = ['title', 'description',]
    date_hierarchy = 'entry_date'
    list_editable = ['entry_date', 'title',  'description', 'value',
                     'shared', 'fixed', 'installments_number', 'id_titular_user', 'id_active_user']
    empty_value_display = 'vazio'
    # list_per_page = 20
    # Preenche o slug automaticamente
    prepopulated_fields = {'slug': ['title']}
    radio_fields = {'id_modality': admin.HORIZONTAL,
                    'id_type': admin.HORIZONTAL, }
    # permite adicionar um input de pesquisa que se auto-completa. Necessário definir na classe do atributos os search_fields que serão utilizados para auto-completar a digitação
    autocomplete_fields = ['id_card']


@admin.register(models.Installment)
class InstallmentAdmin(admin.ModelAdmin):
    list_display = 'id', 'id_entry', 'number', 'value', 'payment_date', 'paid', 'id_titular_user',

    search_fields = ['id', 'id_entry', 'number', 'value',
                     'payment_date', 'paid', 'id_titular_user']
    date_hierarchy = 'payment_date'
    list_editable = ['id_entry', 'number', 'value',
                     'payment_date', 'paid', 'id_titular_user',]
    empty_value_display = 'vazio'


@admin.register(models.Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = 'id', 'id_installment', 'date', 'value', 'id_active_user'


@admin.register(models.Modality)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',


@admin.register(models.Category)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',


@admin.register(models.Type)
class TipoAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',
