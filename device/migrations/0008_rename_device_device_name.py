# Generated by Django 4.1.5 on 2023-02-01 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0007_remove_device_failure'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='device',
            new_name='name',
        ),
    ]
