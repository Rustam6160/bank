# Generated by Django 5.0.1 on 2024-09-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_credit_payoff_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='payoff_date',
            field=models.TextField(default=dict),
        ),
    ]
