# Generated by Django 4.0.4 on 2022-05-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_calendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='cash',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='date_of_the_lesson',
            field=models.DateTimeField(verbose_name='Дата проведения занятия'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='duration',
            field=models.CharField(max_length=100, verbose_name='Время занятия'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='status',
            field=models.CharField(max_length=100, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='date_of_issue',
            field=models.DateTimeField(verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='last_update',
            field=models.DateTimeField(verbose_name='Последняя дата обновления'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birthday',
            field=models.DateField(verbose_name='День рождения'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_update',
            field=models.DateTimeField(verbose_name='Последняя дата обновления'),
        ),
    ]
