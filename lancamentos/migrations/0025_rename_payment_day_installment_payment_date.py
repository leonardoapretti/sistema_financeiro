# Generated by Django 5.1 on 2024-09-08 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lancamentos', '0024_installment_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='installment',
            old_name='payment_day',
            new_name='payment_date',
        ),
    ]
