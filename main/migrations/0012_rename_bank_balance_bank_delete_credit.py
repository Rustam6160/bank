# Generated by Django 5.0.1 on 2024-09-11 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_bank_balance_credit'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bank_balance',
            new_name='Bank',
        ),
        migrations.DeleteModel(
            name='Credit',
        ),
    ]
