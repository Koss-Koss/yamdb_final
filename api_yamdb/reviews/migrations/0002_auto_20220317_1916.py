# Generated by Django 2.2.16 on 2022-03-17 19:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, 'оценка по шкале от 1'), django.core.validators.MaxValueValidator(10, 'оценка по шкале до 10')]),
        ),
    ]
