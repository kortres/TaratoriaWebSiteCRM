from .models import Userinfo, Homework, Calendar
from django.forms import *
from django.contrib.auth.forms import User, UserCreationForm
from django import forms


class MyChoice(forms.ModelChoiceField):
  def label_from_instance(self, obj):
    return obj.get_full_name()


class PickUserForm(forms.Form):

     login = MyChoice(
         queryset=User.objects.exclude(username='kortres').exclude(username='speech').exclude(is_active=False))



class CreateUserCard(ModelForm):
    login = MyChoice(label='Имя пользователя:',
        queryset=User.objects.exclude(username='kortres').exclude(username='speech').exclude(is_active=False))

    card_name = forms.CharField(label='Название карты:')

    birthday = forms.DateField(widget=DateInput(attrs={'autocomplete': 'off'}), label='Дата осмотра:', required=False)

    class Meta:
        model = Userinfo
        fields = ['login', 'card_name', 'birthday', 'pmpk', 'sound_of_speech', 'structure_and_mobility', 'understanding',
                  'sound_state', 'structure_of_the_word', 'dictionary_feature', 'grammatical_structure', 'connected_speech',
                  'general_recommendations']

        widgets = {

            "pmpk": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "sound_of_speech": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "structure_and_mobility": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "understanding": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "sound_state": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "structure_of_the_word": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "dictionary_feature": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "grammatical_structure": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "connected_speech": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "general_recommendations": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),
        }


class UpdateUserCard(ModelForm):
    card_name = forms.CharField(label='Название карты:')

    birthday = forms.DateField(widget=DateInput(attrs={'autocomplete': 'off'}), label='Дата осмотра:', required=False)

    class Meta:
        model = Userinfo
        fields = ['card_name', 'birthday', 'pmpk', 'sound_of_speech', 'structure_and_mobility',
                  'understanding',
                  'sound_state', 'structure_of_the_word', 'dictionary_feature', 'grammatical_structure',
                  'connected_speech',
                  'general_recommendations']

        widgets = {

            "pmpk": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "sound_of_speech": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "structure_and_mobility": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "understanding": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "sound_state": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "structure_of_the_word": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "dictionary_feature": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "grammatical_structure": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "connected_speech": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),

            "general_recommendations": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'

            }),
        }


class CalendarForm(forms.Form):
    login = MyChoice(label='Имя пользователя:',
                                   queryset=User.objects.exclude(username='kortres').exclude(username='speech').exclude(
                                       is_active=False), required=False)
    first_data = forms.DateField(widget=DateInput(attrs={'autocomplete': 'off'}), label='Дата первая:', required=False)
    second_data = forms.DateField(widget=DateInput(attrs={'autocomplete': 'off'}), label='Дата вторая:', required=False)


class CreateCalendarForm(ModelForm):
    login = MyChoice(label='Имя пользователя:',
                                   queryset=User.objects.exclude(username='kortres').exclude(username='speech').exclude(
                                       is_active=False))
    date_of_the_lesson = forms.DateField(widget=DateInput(attrs={'autocomplete': 'off'}), label='Дата вторая:', required=False)

    choises = (
        ('Не проведено', 'Не проведено'),
        ('Проведено', 'Проведено' ),
        ('Не явка', 'Не явка'),
        ('Отменено', 'Отменено')
    )
    status = forms.CharField(label='Стаутс:', widget=Select(choices=choises))

    class Meta:
        model = Calendar

        fields = ['login', 'class_name', 'duration', 'date_of_the_lesson', 'time_of_the_lesson', 'cash', 'status']


class CalendarUpdateForm(ModelForm):

    choises = (
        ('Не проведено', 'Не проведено'),
        ('Проведено', 'Проведено'),
        ('Не явка', 'Не явка'),
        ('Отменено', 'Отменено')
    )
    status = forms.CharField(label='Стаутс:', widget=Select(choices=choises))

    class Meta:
        model = Calendar

        fields = ['class_name', 'duration', 'date_of_the_lesson', 'time_of_the_lesson', 'cash', 'status']


class StatisticsForm(forms.Form):
    first_data = forms.DateField(widget=DateInput(attrs={'autocomplete': 'off'}), label='Дата первая:')
    second_data = forms.DateField(widget=DateInput(attrs={'autocomplete': 'off'}), label='Дата вторая:')


class CreateHomeworkForm(ModelForm):
    login = MyChoice(label='Имя пользователя:',
                                   queryset=User.objects.exclude(username='kortres').exclude(username='speech').exclude(
                                       is_active=False))

    date_of_issue = forms.DateTimeField(widget=DateTimeInput(attrs={'autocomplete': 'off'}), label='Дата создания:')

    last_update = forms.DateTimeField(widget=DateTimeInput(attrs={'autocomplete': 'off'}), label='Дата посленего обновления:')

    class Meta:
        model = Homework
        fields = ['login', 'homework_name', 'date_of_issue', 'last_update', 'homework']

        widgets={
            "homework": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'
            }),
        }


class UpdateHomeworkForm(ModelForm):

    date_of_issue = forms.DateTimeField(widget=DateTimeInput(attrs={'autocomplete': 'off'}), label='Дата создания:')

    last_update = forms.DateTimeField(widget=DateTimeInput(attrs={'autocomplete': 'off'}), label='Дата посленего обновления:')

    class Meta:
        model = Homework
        fields = ['homework_name', 'date_of_issue', 'last_update', 'homework']

        widgets={
            "homework": Textarea(attrs={
                'class': 'form_control mb-2',
                'style': 'min-width: 60vh'
            }),
        }


class Registration(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    is_active = forms.CheckboxInput()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'is_active')
