from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = 'id', 'data_lancamento', 'titulo',  'descricao', 'quantidade_parcelas',  'valor_total', 'id_categoria', 'id_instituicao_financeira', 'id_modalidade', 'id_tipo', 'compartilhado', 'fixo_mensal', 'id_usuario_titular', 'id_usuario_ativo', 'slug'
    list_filter = ['data_lancamento', 'compartilhado',
                   'quantidade_parcelas', 'descricao', 'id_categoria', 'id_modalidade']
    search_fields = ['titulo', 'descricao',]
    date_hierarchy = 'data_lancamento'
    list_editable = ['data_lancamento', 'titulo',  'descricao', 'valor_total',
                     'compartilhado', 'fixo_mensal', 'quantidade_parcelas', 'id_usuario_titular', 'id_usuario_ativo']
    empty_value_display = 'vazio'
    list_per_page = 20
    # Preenche o slug automaticamente
    prepopulated_fields = {'slug': ['titulo']}
    radio_fields = {'id_modalidade': admin.HORIZONTAL,
                    'id_tipo': admin.HORIZONTAL, }
    # permite adicionar um input de pesquisa que se auto-completa. Necessário definir na classe do atributos os search_fields que serão utilizados para auto-completar a digitação
    autocomplete_fields = ['id_instituicao_financeira']
    # fields = [('titulo',  'descricao',), ('compartilhado', 'fixo_mensal')] # os campos que serão exibidos ao clicar no item. A organização em tuplas significa que os itens serão alinhados na mesma linha
    # fieldsets = [  # parte de adicionar ou editar itens
    #     (
    #         'Características',
    #         {
    #             "fields": ['data_lancamento', 'titulo',  'descricao', 'valor_total', 'quantidade_parcelas'],
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


@admin.register(models.LancamentoBaixa)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = 'id', 'id_lancamento', 'data', 'valor', 'numero_parcela',


@admin.register(models.Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome',


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome',


@admin.register(models.Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome',


@admin.register(models.InstituicaoFincanceira)
class InstituicaoFincanceiraAdmin(admin.ModelAdmin):
    list_display = 'id', 'nome',
    search_fields = ['nome']


# admin.site.register(models.Usuario)
admin.site.register(models.Parcela)

# @admin.register(models.Categoria)
# class CategoriaAdmin(admin.ModelAdmin):
#     ...


# @admin.register(models.InstituicaoFincanceira)
# class InstituicaoAdmin(admin.ModelAdmin):
#     ...

# @admin.register(models.Tipo)
# class TipoAdmin:
#     ...
