# Generated by Django 2.2.4 on 2019-11-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20191115_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='item_json',
            new_name='items_json',
        ),
        migrations.AlterField(
            model_name='order',
            name='address2',
            field=models.CharField(default='', max_length=100),
        ),
    ]
