# Generated by Django 4.0.4 on 2022-05-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0019_alter_userinfo_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='connected_speech',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Связная речь:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='dictionary_feature',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Характеристика словаря:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='general_recommendations',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Рекомендации:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='grammatical_structure',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Грамматический строй речи:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pmpk',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Заключение ПМПК:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sound_of_speech',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Общее звучание речи:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='sound_state',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Состояние звукопроизношения:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='structure_and_mobility',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Строение и подвижность органов артикуляции:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='structure_of_the_word',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Слоговая структура слова:'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='understanding',
            field=models.TextField(blank=True, max_length=2000, verbose_name='Понимание речи:'),
        ),
    ]
