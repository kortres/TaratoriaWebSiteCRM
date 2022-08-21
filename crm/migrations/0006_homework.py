# Generated by Django 4.0.4 on 2022-05-10 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crm', '0005_delete_homework'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homework_name', models.CharField(max_length=100, verbose_name='Название домашнего задания')),
                ('date_of_issue', models.DateTimeField(verbose_name='Дата создания')),
                ('last_update', models.DateTimeField(verbose_name='Последняя дата обновления')),
                ('homework', models.TextField(max_length=500, verbose_name='Домашние задание')),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Домашнее задание',
                'verbose_name_plural': 'Домашние задания',
            },
        ),
    ]