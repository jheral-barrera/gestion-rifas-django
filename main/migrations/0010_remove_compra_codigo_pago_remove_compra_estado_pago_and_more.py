# Generated by Django 4.2.7 on 2023-11-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_compra_codigo_pago'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='codigo_pago',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='estado_pago',
        ),
        migrations.AddField(
            model_name='numero',
            name='codigo_pago',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='numero',
            name='estado_pago',
            field=models.CharField(blank=True, choices=[('pagado', 'Pagado'), ('reservado', 'Reservado')], max_length=10, null=True),
        ),
    ]
