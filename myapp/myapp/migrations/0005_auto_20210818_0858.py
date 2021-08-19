# Generated by Django 3.0.5 on 2021-08-18 08:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20210818_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='mob_no',
            field=models.IntegerField(validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
