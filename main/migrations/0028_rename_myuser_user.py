# Generated by Django 5.0.1 on 2024-09-26 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_rename_user_myuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MyUser',
            new_name='User',
        ),
    ]
