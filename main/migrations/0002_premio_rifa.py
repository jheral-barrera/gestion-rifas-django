# Generated by Django 4.2.7 on 2023-11-20 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='premio',
            name='rifa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.rifa'),
            preserve_default=False,
        ),
    ]
