# Generated by Django 5.0.1 on 2024-09-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_credit_payoff_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='money_back_month',
            field=models.IntegerField(default=0),
        ),
    ]
