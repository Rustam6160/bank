# Generated by Django 5.0.1 on 2024-09-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_credit_how_many_months'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='how_many_months',
            field=models.PositiveIntegerField(),
        ),
    ]
