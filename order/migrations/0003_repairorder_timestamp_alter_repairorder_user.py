# Generated by Django 4.1.5 on 2023-01-12 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairorder',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date of the order'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='repairorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Technical'),
        ),
    ]