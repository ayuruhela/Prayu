# Generated by Django 2.2.4 on 2019-11-11 04:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dpofile',
            new_name='Dprofile',
        ),
    ]
