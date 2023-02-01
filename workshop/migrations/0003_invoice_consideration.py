# Generated by Django 4.1.5 on 2023-02-01 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_alter_assignment_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Amount')),
                ('warranty_days', models.SmallIntegerField(default=15, verbose_name='Warranty Days')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Creation Date')),
                ('delivery_date', models.DateField(blank=True, null=True, verbose_name='Delivery Date')),
                ('assignment', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='workshop.assignment')),
            ],
            options={
                'db_table': 'invoice',
            },
        ),
        migrations.CreateModel(
            name='Consideration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=512, null=True, verbose_name='Note')),
                ('invoice', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workshop.invoice')),
            ],
            options={
                'db_table': 'consideration',
            },
        ),
    ]