# Generated by Django 3.0.5 on 2020-04-26 08:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0004_auto_20200422_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
