from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from bank_account.models import CardModel, BankAccountModel


class Category(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=65)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Type(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Modality(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=65)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Entry(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)  # ok
    title = models.CharField(max_length=65, verbose_name='Titulo')  # ok
    description = models.CharField(
        max_length=165, null=True, default=None, blank=True, verbose_name='Descrição')  # ok
    value = models.FloatField(verbose_name='Valor')  # ok
    slug = models.SlugField(unique=True)
    entry_date = models.DateField(
        null=True, default=date.today(), verbose_name='Data')  # ok
    created_at = models.DateTimeField(auto_now_add=True)
    shared = models.BooleanField(default=False, verbose_name='Compartilhado')
    fixed = models.BooleanField(default=False, verbose_name='Fixo')
    installments_number = models.PositiveIntegerField(
        default=1, verbose_name='Quantidade de parcelas')
    id_category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Categoria')
    id_card = models.ForeignKey(
        CardModel, on_delete=models.DO_NOTHING, verbose_name='Cartao', default=None, null=True, blank=True, )
    id_bank_account = models.ForeignKey(
        BankAccountModel, on_delete=models.DO_NOTHING, default=None, null=True, blank=True, verbose_name='Banco')
    id_modality = models.ForeignKey(
        Modality, on_delete=models.CASCADE, verbose_name='Modalidade', default=1)
    id_type = models.ForeignKey(
        Type, on_delete=models.CASCADE, verbose_name='Tipo', default=2)
    id_active_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='users_to_usuario_ativo', verbose_name='Usuario ativo')
    id_titular_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='users_to_usuario_titular', verbose_name='Titular')

    class Meta:
        verbose_name = 'Lançamento'
        ordering = ['-entry_date']

    def __str__(self):
        return self.title

    def __set_slug(self):
        if not self.slug:
            slug = f'{slugify(self.title)}'
            exist_slug = Entry.objects.filter(slug=slug).first()
            if exist_slug is not None:
                slug += f'-{get_random_string(4)}'
            self.slug = slug

    def save(self, *args, **kwargs):
        self.__set_slug()
        # TODO VERIFICAR SE É MELHOR DEIXAR ASSIM OU CONFORME ENTRADA DO USUÁRIO
        self.title = self.title.capitalize()
        self.description = self.description.capitalize()

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('lancamentos:detalhes', args=(self.id,))


# class LancamentoBaixa(models.Model):
#     id = models.AutoField(primary_key=True, editable=False)
#     id_parcela = models.ForeignKey(Entry, on_delete=models.CASCADE)
#     data = models.DateTimeField(auto_now_add=True)
#     valor = models.FloatField()
#     numero_parcela = models.PositiveIntegerField(default=1)

#     class Meta:
#         verbose_name = 'Lançamento Baixa'
#         verbose_name_plural = 'Lançamentos Baixas'

#     def __str__(self):
#         return self.id


# class Installment(models.Model):
#     id = models.AutoField(primary_key=True, editable=False)
#     id_lancamento = models.ForeignKey(Entry, on_delete=models.CASCADE)
#     numero_parcela = models.PositiveIntegerField()
#     valor_parcela = models.FloatField()
#     data_vencimento = models.DateField()
