# Generated by Django 3.1 on 2020-09-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_orders_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(max_length=120),
        ),
    ]
