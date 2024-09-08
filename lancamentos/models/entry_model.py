from django.urls import reverse
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from bank_account.models import CardModel, BankAccountModel
from .other_models import Category, Type, Modality


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
        Category, on_delete=models.CASCADE, verbose_name='Categoria', default=None, null=True, blank=True, )
    id_card = models.ForeignKey(
        CardModel, on_delete=models.SET_NULL, verbose_name='Cartao', default=None, null=True, blank=True, )
    id_bank_account = models.ForeignKey(
        BankAccountModel, on_delete=models.SET_NULL, default=None, null=True, blank=True, verbose_name='Banco')
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
        self.title = self.title.capitalize()
        self.description = self.description.capitalize(
        ) if self.description else self.description

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('lancamentos:detalhes', args=(self.id,))
