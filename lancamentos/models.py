from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from datetime import date


# class Usuario(models.Model):
#     usuario = models.OneToOneField(
#         User, on_delete=models.CASCADE, related_name='perfil', unique=True)
#     # TODO alterar para required após desenvovimento
#     cpf = models.PositiveIntegerField()
#     telefone = models.PositiveIntegerField(null=True, default=None)

#     def __str__(self) -> str:
#         return self.usuario.get_full_name()


class Categoria(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=65)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class InstituicaoFincanceira(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=65)

    class Meta:
        verbose_name = 'Instituição Financeira'
        verbose_name_plural = 'Instituições Financeiras'

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Tipo(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.nome

    class Meta:
        ordering = ['nome']


class Modalidade(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nome = models.CharField(max_length=65)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Lancamento(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)  # ok
    titulo = models.CharField(max_length=65, verbose_name='Titulo')  # ok
    descricao = models.CharField(
        max_length=165, null=True, default=None, blank=True)  # ok
    valor_total = models.FloatField(verbose_name='Valor')  # ok
    slug = models.SlugField(unique=True)
    data_lancamento = models.DateField(
        null=True, default=date.today(), verbose_name='Data')  # ok
    data_criacao = models.DateTimeField(auto_now_add=True)
    compartilhado = models.BooleanField(default=False)
    fixo_mensal = models.BooleanField(default=False)
    quantidade_parcelas = models.PositiveIntegerField(
        default=1, verbose_name='Quantidade de parcelas')
    # valor_quitado = models.FloatField()
    id_categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, verbose_name='Categoria')
    id_instituicao_financeira = models.ForeignKey(
        InstituicaoFincanceira, on_delete=models.CASCADE, verbose_name='Instituição financeira')
    id_modalidade = models.ForeignKey(
        Modalidade, on_delete=models.CASCADE, verbose_name='Modalidade', default=1)
    id_tipo = models.ForeignKey(
        Tipo, on_delete=models.CASCADE, verbose_name='Tipo', default=2)
    id_usuario_ativo = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='users_to_usuario_ativo', verbose_name='Usuario ativo')
    id_usuario_titular = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='users_to_usuario_titular', verbose_name='Titular')

    class Meta:
        verbose_name = 'Lançamento'
        ordering = ['-data_lancamento']

    def __str__(self):
        return self.titulo

    def __set_slug(self):
        if not self.slug:
            slug = f'{slugify(self.titulo)}'
            slug_existente = Lancamento.objects.filter(slug=slug).first()
            if slug_existente is not None:
                slug += f'-{get_random_string(4)}'
            self.slug = slug

    def __set_first_caracter_uppercase(self):
        print(self.titulo.capitalize())

    def save(self, *args, **kwargs):
        self.__set_slug()
        # TODO VERIFICAR SE É MELHOR DEIXAR ASSIM OU CONFORME ENTRADA DO USUÁRIO
        self.titulo = self.titulo.capitalize()
        self.descricao = self.descricao.capitalize()

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('lancamentos:detalhes', args=(self.id,))


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
