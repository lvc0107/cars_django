# Generated by Django 3.0.6 on 2020-06-02 01:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('create_at', models.DateTimeField(default=datetime.datetime(2020, 6, 2, 1, 10, 50, 391075, tzinfo=utc))),
            ],
        ),
    ]
