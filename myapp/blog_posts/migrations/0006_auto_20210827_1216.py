# Generated by Django 3.0.5 on 2021-08-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0005_auto_20210827_0927'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'managed': True, 'ordering': ['email']},
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
