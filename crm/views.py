from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import User
from django.views.generic import *
from django.db.models import Avg, Count, Min, Sum


def crm_index(request):
    return render(request, 'crm/index.html')


def create_user_card(request):
    error = ''
    if request.method == 'POST':
        form = CreateUserCard(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crm/user_card')
        else:
            error = 'Форма заполнена неверно'
    form = CreateUserCard()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'crm/create_user_card.html', data)


def user_card(request):
    data = {}

    if request.user.username == 'speech':
        if request.method == 'GET':
            form = PickUserForm(request.GET)
            if form.is_valid():
                    news = Userinfo.objects.filter(login=request.GET.get('login')).order_by('card_name')
                    data = {
                        'form': form,
                        'news': news
                    }
            else:
                form = PickUserForm()
                data = {
                    'form': form,
                }

    else:
        user_data = Userinfo.objects.filter(login=request.user.id).order_by('card_name')
        data = {
            'user_data': user_data
        }
    return render(request, 'crm/user_card.html', data)


def calendar(request):
    data={}
    user = User.objects.all()
    if request.user.username == 'speech':
        if request.method == 'GET':
            form = CalendarForm(request.GET)
            if request.GET.get('second_data') == None and request.GET.get('first_data') == None and request.GET.get('login') == None:
                form = CalendarForm()
                news = Calendar.objects.filter(login__is_active=True).order_by('date_of_the_lesson')
                data= {
                    'form': form,
                    'news': news,
                    'user': user
                }
            else:
                if request.GET.get('login') == "":
                    if request.GET.get('second_data') == "" and request.GET.get('first_data') != "":
                        news = Calendar.objects.filter(login__is_active=True).filter(date_of_the_lesson=request.GET.get('first_data')).order_by(
                            'date_of_the_lesson')
                        data = {
                            'form': form,
                            'news': news,
                            'user': user
                        }
                    elif request.GET.get('second_data') != "" and request.GET.get('first_data') != "":
                        news = Calendar.objects.filter(login__is_active=True).filter(
                            date_of_the_lesson__range=[request.GET.get('first_data'),
                                                       request.GET.get('second_data')]).order_by('date_of_the_lesson')
                        data = {
                            'form': form,
                            'news': news,
                            'user': user
                        }
                    else:
                        form = CalendarForm()
                        news = Calendar.objects.all().filter(login__is_active=True).order_by('date_of_the_lesson')
                        data = {
                            'form': form,
                            'news': news,
                            'user': user
                        }
                else:
                    if request.GET.get('second_data') == "" and request.GET.get('first_data') != "":
                        news = Calendar.objects.filter(login__is_active=True).filter(date_of_the_lesson=request.GET.get('first_data')).filter(login=request.GET.get('login')).order_by(
                            'date_of_the_lesson')
                        data = {
                            'form': form,
                            'news': news,
                            'user': user
                        }
                    elif request.GET.get('second_data') != "" and request.GET.get('first_data') != "":
                        news = Calendar.objects.filter(login__is_active=True).filter(
                            date_of_the_lesson__range=[request.GET.get('first_data'),
                                                       request.GET.get('second_data')]).filter(login=request.GET.get('login')).order_by('date_of_the_lesson')
                        data = {
                            'form': form,
                            'news': news,
                            'user': user
                        }
                    else:
                        form = CalendarForm()
                        news = Calendar.objects.filter(login__is_active=True).filter(login=request.GET.get('login')).order_by('date_of_the_lesson')
                        data = {
                            'form': form,
                            'news': news,
                            'user': user
                        }
    else:
        form = CalendarForm()
        news = Calendar.objects.filter(login=request.user.id).order_by('date_of_the_lesson')
        data = {
            'form': form,
            'news': news,
            'user': user
        }
    return render(request, 'crm/calendar.html', data)


def create_calendar(request):
    error = ''
    if request.method == 'POST':
        form = CreateCalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crm/create_calendar')
        else:
            error = 'Форма заполнена неверно'
    form = CreateCalendarForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'crm/create_calendar.html', data)


def create_homework(request):
    error = ''
    if request.method == 'POST':
        form = CreateHomeworkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/crm/create_homework')
        else:
            error = 'Форма заполнена неверно'
    form = CreateHomeworkForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'crm/create_homework.html', data)


def homework(request):
    data={}

    if request.user.username == 'speech':
        if request.method == 'GET':
            form = PickUserForm(request.GET)
            if form.is_valid():
                news = Homework.objects.filter(login=request.GET.get('login')).order_by('homework_name')
                data = {
                    'form': form,
                    'news': news
                }
            else:
                form = PickUserForm()
                data = {
                    'form': form,
                }

    else:
        user_data = Homework.objects.filter(login=request.user.id).order_by('homework_name')
        data = {
            'user_data': user_data
        }
    return render(request, 'crm/homework.html', data)


def user_profile(request):

    if request.user.username == 'speech':
        form = User.objects.exclude(username='kortres').exclude(username='speech')
        data = {
            'form': form
        }
    else:
        form = User.objects.filter(id=request.user.id)
        data = {
            'form': form
        }
    return render(request, 'crm/user_profile.html', data)


def archive(request):
    form = User.objects.filter(is_active='False')
    news = Userinfo.objects.all()
    data = {
        'form': form,
        'news': news
    }
    return render(request, 'crm/archive.html', data)


def statistics(request):
    data = {}

    if request.user.username == 'speech':
        if request.method == 'GET':
            form = StatisticsForm(request.GET)
            if form.is_valid():
                users_count = Calendar.objects.filter(date_of_the_lesson__range=[request.GET.get('first_data'), request.GET.get('second_data')]).filter(status='Проведено').aggregate(Count('login', distinct=True))
                users = User.objects.filter(calendar__status='Проведено').distinct()
                hour = Calendar.objects.filter(date_of_the_lesson__range=[request.GET.get('first_data'), request.GET.get('second_data')]).filter(status='Проведено').aggregate(Sum('duration'))
                classes_counts = Calendar.objects.filter(date_of_the_lesson__range=[request.GET.get('first_data'), request.GET.get('second_data')]).filter(status='Проведено').count()
                cash_sum = Calendar.objects.filter(date_of_the_lesson__range=[request.GET.get('first_data'), request.GET.get('second_data')]).filter(status='Проведено').aggregate(Sum('cash'))
                data = {
                    'form': form,
                    'users_count': users_count,
                    'users': users,
                    'classes_counts': classes_counts,
                    'cash_sum': cash_sum,
                    'hour': hour
                }
            else:
                form = StatisticsForm()
                data = {
                    'form': form,
                }
    return render(request, 'crm/statistics.html', data)


class UserCardDetails(DetailView):
    model = Userinfo
    template_name = 'crm/user_card_details.html'
    context_object_name = 'user_card_details'


class UserCardUpdate(UpdateView):
    model = Userinfo
    form_class = UpdateUserCard
    template_name = 'crm/user_card_update.html'


class UserCardDelete(DeleteView):
    model = Userinfo
    success_url = '/crm/user_card'
    template_name = 'crm/user_card_delete.html'


class HomeworkUpdate(UpdateView):
    model = Homework
    form_class = UpdateHomeworkForm
    template_name = 'crm/homework_update.html'


class HomeworkDelete(DeleteView):
    model = Homework
    success_url = '/crm/homework'
    template_name = 'crm/homework_delete.html'


class UserProfileUpdate(UpdateView):
    model = User
    template_name = 'crm/user_profile_update.html'

    fields = ['username', 'first_name', 'last_name']


class UserProfileUpdateSpeech(UpdateView):
    model = User
    template_name = 'crm/user_profile_update_speech.html'

    fields = ['username', 'first_name', 'last_name', 'is_active']


class UserProfileDeleteSpeech(DeleteView):
    model = User
    success_url = '/crm/user_profile'
    template_name = 'crm/user_profile_delete_speech.html'


class CreateUser(CreateView):
    form_class = Registration
    success_url = '/crm/user_profile'
    template_name = "crm/create_user.html"


class CalendarUpdate(UpdateView):
    model = Calendar
    form_class = CalendarUpdateForm
    template_name = 'crm/calendar_update.html'


class CalendarDelete(DeleteView):
    model = Calendar
    success_url = '/crm/calendar'
    template_name = 'crm/calendar_delete.html'
