# Generated by Django 5.0.4 on 2024-07-14 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_venta_productos_venta_total_usd_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto_venta',
            name='total_usd',
        ),
    ]
