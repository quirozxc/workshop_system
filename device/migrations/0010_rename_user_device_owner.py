# Generated by Django 4.1.5 on 2023-02-01 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0009_delete_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='user',
            new_name='owner',
        ),
    ]