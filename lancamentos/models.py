from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=65)

    def __str__(self):
        return self.nome


class InstituicaoFincanceira(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=65)

    class Meta:
        verbose_name = 'Instituição Financeira'
        verbose_name_plural = 'Instituições Financeiras'

    def __str__(self):
        return self.nome


class Tipo(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.nome


class Modalidade(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=65)

    def __str__(self):
        return self.nome


class Lancamento(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    titulo = models.CharField(max_length=65)
    descricao = models.CharField(max_length=165, null=True, default=None)
    valor_total = models.FloatField(verbose_name='Valor')
    slug = models.SlugField()  # voltar para unique=True após desenvolvimento
    data_lancamento = models.DateField(
        null=True, default=None, verbose_name='Data')
    data_criacao = models.DateTimeField(auto_now_add=True)
    compartilhado = models.BooleanField(default=False)
    fixo_mensal = models.BooleanField(default=False)
    quantidade_parcelas = models.PositiveIntegerField(
        default=1, verbose_name='Quantidade de parcelas')

    id_categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    id_instituicao_financeira = models.ForeignKey(
        InstituicaoFincanceira, on_delete=models.CASCADE, verbose_name='Instituição financeira')
    id_modalidade = models.ForeignKey(
        Modalidade, on_delete=models.CASCADE, verbose_name='Modalidade')
    id_tipo = models.ForeignKey(
        Tipo, on_delete=models.CASCADE, verbose_name='Tipo')
    id_usuario_ativo = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='users_to_usuario_ativo')
    id_usuario_titular = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='users_to_usuario_titular', verbose_name='Titular')

    class Meta:
        verbose_name = 'Lançamento'

    def __str__(self):
        return self.titulo


class LancamentoBaixa(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_lancamento = models.ForeignKey(Lancamento, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    valor = models.FloatField()
    numero_parcela = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Lançamento Baixa'
        verbose_name_plural = 'Lançamentos Baixas'

    def __str__(self):
        return self.id


class Parcela(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    id_lancamento = models.ForeignKey(Lancamento, on_delete=models.CASCADE)
    numero_parcela = models.PositiveIntegerField()
    valor_parcela = models.FloatField()
    data_vencimento = models.DateField()
