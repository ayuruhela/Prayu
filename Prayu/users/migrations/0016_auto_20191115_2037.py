# Generated by Django 2.2.4 on 2019-11-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20191115_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdate',
            name='order_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]