# Generated by Django 4.1.5 on 2023-05-19 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0007_remove_assignment_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='delivery_date',
            new_name='pickup_date',
        ),
    ]
