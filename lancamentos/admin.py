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
    list_per_page = 20
    # Preenche o slug automaticamente
    prepopulated_fields = {'slug': ['title']}
    radio_fields = {'id_modality': admin.HORIZONTAL,
                    'id_type': admin.HORIZONTAL, }
    # permite adicionar um input de pesquisa que se auto-completa. Necessário definir na classe do atributos os search_fields que serão utilizados para auto-completar a digitação
    autocomplete_fields = ['id_card']
    # fields = [('title',  'description',), ('compartilhado', 'fixed')] # os campos que serão exibidos ao clicar no item. A organização em tuplas significa que os itens serão alinhados na mesma linha
    # fieldsets = [  # parte de adicionar ou editar itens
    #     (
    #         'Características',
    #         {
    #             "fields": ['data_lancamento', 'title',  'description', 'value', 'installment_number'],
    #         },
    #     ),
    #     (
    #         "Boolean",
    #         {
    #             "fields": [('compartilhado', 'fixo_mensal')],
    #         },
    #     ),
    #     (
    #         "Usuários",
    #         {
    #             "classes": ["collapse"],
    #             "fields": ['id_usuario_titular', 'id_usuario_ativo'],
    #         },
    #     ),
    # ]


# @admin.register(models.LancamentoBaixa)
# class LancamentoAdmin(admin.ModelAdmin):
#     list_display = 'id', 'id_parcela', 'data', 'valor', 'numero_parcela',


@admin.register(models.Modality)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',


@admin.register(models.Category)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',


@admin.register(models.Type)
class TipoAdmin(admin.ModelAdmin):
    list_display = 'id', 'title',
