from django.db import models


class Userinfo(models.Model):
    login = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    card_name = models.CharField('Карта:',max_length=100)
    birthday = models.DateField('Дата осмотра:', blank=True, null=True)
    pmpk = models.TextField('Заключение ПМПК:', max_length=2000, blank=True)
    sound_of_speech = models.TextField('Общее звучание речи:', max_length=2000, blank=True)
    structure_and_mobility = models.TextField('Строение и подвижность органов артикуляции:', max_length=2000, blank=True)
    understanding = models.TextField('Понимание речи:', max_length=2000, blank=True)
    sound_state = models.TextField('Состояние звукопроизношения:', max_length=2000, blank=True)
    structure_of_the_word = models.TextField('Слоговая структура слова:', max_length=2000, blank=True)
    dictionary_feature = models.TextField('Характеристика словаря:', max_length=2000, blank=True)
    grammatical_structure = models.TextField('Грамматический строй речи:', max_length=2000, blank=True)
    connected_speech = models.TextField('Связная речь:', max_length=2000, blank=True)
    general_recommendations = models.TextField('Рекомендации:', max_length=2000, blank=True)

    def __str__(self):
        return  self.card_name

    def get_absolute_url(self):
        return f'/crm/user_card/{self.id}'

    class Meta:
        verbose_name = 'Информация о пользователе'
        verbose_name_plural = 'Информация о пользователях'


class Homework(models.Model):
    login = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    homework_name = models.CharField('Название домашнего задания:', max_length=100)
    date_of_issue = models.DateTimeField('Дата создания:', blank=True, null=True)
    last_update = models.DateTimeField('Последняя дата обновления:', blank=True, null=True)
    homework = models.TextField('Домашние задание:', max_length=500, blank=True)

    def __str__(self):
        return  self.homework_name

    def get_absolute_url(self):
        return '/crm/homework'

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'


class Calendar(models.Model):
    login = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    class_name = models.CharField('Название занятия:',max_length=100)
    duration = models.FloatField('Длительность занятия:',max_length=100, blank=True, null=True)
    date_of_the_lesson = models.DateField('Дата проведения занятия:', blank=True, null=True)
    time_of_the_lesson = models.CharField('Время начала занятия:', max_length=100, blank=True)
    cash = models.IntegerField('Цена:', blank=True, null=True)
    status = models.CharField('Статус:', max_length=100, blank=True)

    def get_absolute_url(self):
        return '/crm/calendar'


    def __str__(self):
        return  self.class_name


    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'