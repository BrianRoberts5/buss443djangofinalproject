# Generated by Django 4.2 on 2023-04-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0004_course_remove_studentdatafixed_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdatafixed',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, auto_created=True),
        ),
    ]
