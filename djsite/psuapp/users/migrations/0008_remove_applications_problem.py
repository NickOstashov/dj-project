# Generated by Django 4.1.3 on 2022-12-08 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_applications_problem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='problem',
        ),
    ]
