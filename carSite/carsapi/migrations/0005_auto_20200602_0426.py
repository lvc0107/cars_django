# Generated by Django 3.0.6 on 2020-06-02 04:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carsapi', '0004_auto_20200602_0230'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarsUsers',
            new_name='Profile',
        ),
    ]
