# Generated by Django 4.2.7 on 2023-11-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_compra_estado_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='codigo_pago',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
