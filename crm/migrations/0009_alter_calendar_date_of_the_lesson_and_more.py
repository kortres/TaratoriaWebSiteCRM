# Generated by Django 4.0.4 on 2022-05-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_calendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='date_of_the_lesson',
            field=models.DateField(verbose_name='Дата проведения занятия'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birthday',
            field=models.DateField(blank=True, verbose_name='День рождения'),
        ),
    ]
