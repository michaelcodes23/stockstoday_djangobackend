# Generated by Django 3.2.6 on 2021-08-21 04:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='tickerarray',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=25), size=None),
        ),
    ]
