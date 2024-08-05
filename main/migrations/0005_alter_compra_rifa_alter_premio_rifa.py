# Generated by Django 4.2.7 on 2023-11-24 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_compra_rifa_alter_premio_imagen_premio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='rifa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.rifa'),
        ),
        migrations.AlterField(
            model_name='premio',
            name='rifa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.rifa'),
        ),
    ]
