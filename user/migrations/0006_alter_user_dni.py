# Generated by Django 4.1.5 on 2023-05-22 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_phonenumber_is_whatsapp_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dni',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='Identification Document'),
        ),
    ]