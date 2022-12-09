# Generated by Django 4.1.3 on 2022-12-09 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psu', '0014_alter_typeproblem_options'),
        ('users', '0008_remove_applications_problem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='additional_info',
        ),
        migrations.AlterField(
            model_name='applications',
            name='kind_of_problem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='psu.problem', verbose_name='Вариант проблемы'),
        ),
    ]
