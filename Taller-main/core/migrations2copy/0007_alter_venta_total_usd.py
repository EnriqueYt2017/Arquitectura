# Generated by Django 5.0.4 on 2024-07-14 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_venta_total_usd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='total_usd',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=1000),
        ),
    ]