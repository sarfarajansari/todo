# Generated by Django 3.1.4 on 2021-06-05 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claySchedule', '0004_day_lecture_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='day',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='time',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
    ]
