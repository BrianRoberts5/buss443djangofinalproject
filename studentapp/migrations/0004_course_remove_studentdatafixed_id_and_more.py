# Generated by Django 4.2 on 2023-04-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0003_studentdata_alter_studentdatafixed_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('CourseID', models.IntegerField(primary_key=True, serialize=False)),
                ('CourseTitle', models.CharField(max_length=50)),
                ('CourseName', models.CharField(max_length=50)),
                ('CourseSectionCode', models.IntegerField()),
                ('CourseDepartment', models.CharField(max_length=50)),
                ('Instructor', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='studentdatafixed',
            name='id',
        ),
        migrations.AlterField(
            model_name='studentdatafixed',
            name='StudentID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
