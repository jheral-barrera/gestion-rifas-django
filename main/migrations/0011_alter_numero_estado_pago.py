# Generated by Django 4.2.7 on 2023-11-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_compra_codigo_pago_remove_compra_estado_pago_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numero',
            name='estado_pago',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
