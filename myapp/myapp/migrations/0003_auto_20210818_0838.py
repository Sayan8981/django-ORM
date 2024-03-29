# Generated by Django 3.0.5 on 2021-08-18 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_book_list_student_details_student_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book_list',
            options={'managed': True, 'ordering': ['book_name']},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'managed': True, 'ordering': ['name', 'roll_no', 'stud_class', 'department']},
        ),
        migrations.AlterModelOptions(
            name='student_subject',
            options={'managed': True, 'ordering': ['student', 'subject']},
        ),
        migrations.AlterField(
            model_name='book_list',
            name='book_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='stud_class',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='address',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='father_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='mob_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='mother_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='student_subject',
            name='subject',
            field=models.CharField(max_length=20),
        ),
    ]
