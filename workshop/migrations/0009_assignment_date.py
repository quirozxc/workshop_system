# Generated by Django 4.1.5 on 2023-06-14 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0008_rename_delivery_date_invoice_pickup_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
    ]
