# Generated by Django 5.1 on 2024-08-30 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0001_initial'),
        ('lancamentos', '0002_alter_entry_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='id_card',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bank_account.cardmodel', verbose_name='Cartao'),
            preserve_default=False,
        ),
    ]
