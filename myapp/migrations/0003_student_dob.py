# Generated by Django 5.0.3 on 2024-03-17 08:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_course_alter_student_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(default=datetime.date(2000, 1, 1)),
        ),
    ]
