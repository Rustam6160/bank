# Generated by Django 5.0.1 on 2024-09-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='00000000', max_length=8),
        ),
    ]
