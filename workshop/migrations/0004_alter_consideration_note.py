# Generated by Django 4.1.5 on 2023-02-01 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0003_invoice_consideration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consideration',
            name='note',
            field=models.TextField(blank=True, max_length=512, null=True, verbose_name='Note'),
        ),
    ]
