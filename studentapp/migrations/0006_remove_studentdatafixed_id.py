# Generated by Django 4.2 on 2023-04-27 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0005_auto_20230427_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentdatafixed',
            name='id',
        ),
    ]
