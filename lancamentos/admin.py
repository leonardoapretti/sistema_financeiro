from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Lancamento)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = 'id', 'titulo', 'data_lancamento', 'data_criacao', 'valor_total', 'compartilhado', 'fixo_mensal', 'quantidade_parcelas',


@admin.register(models.LancamentoBaixa)
class LancamentoAdmin(admin.ModelAdmin):
    list_display = 'id', 'id_lancamento', 'data', 'valor', 'numero_parcela',


admin.site.register(models.Categoria)
admin.site.register(models.Tipo)
admin.site.register(models.InstituicaoFincanceira)
admin.site.register(models.Modalidade)
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
