# Generated by Django 3.2.6 on 2021-08-28 02:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tickerarray',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), size=None),
        ),
    ]
