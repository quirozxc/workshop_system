# Generated by Django 4.1.5 on 2023-05-22 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_user_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dni',
            field=models.PositiveIntegerField(verbose_name='Identification Document'),
        ),
    ]
