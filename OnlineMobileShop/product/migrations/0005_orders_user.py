# Generated by Django 3.1 on 2020-10-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200928_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.CharField(default='noname', max_length=15),
            preserve_default=False,
        ),
    ]