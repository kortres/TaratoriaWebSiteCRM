from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index', views.crm_index, name='crm_index'),
    path('user_card', views.user_card, name='user_card'),
    path('create_user_card', views.create_user_card, name='create_user_card'),
    path('user_card/<int:pk>', views.UserCardDetails.as_view(), name='user_card_details'),
    path('user_card/<int:pk>/update', views.UserCardUpdate.as_view(), name='user_card_update'),
    path('user_card/<int:pk>/delete', views.UserCardDelete.as_view(), name='user_card_delete'),
    path('calendar', views.calendar, name='calendar'),
    path('create_calendar', views.create_calendar, name='create_calendar'),
    path('calendar/<int:pk>/update', views.CalendarUpdate.as_view(), name='calendar_update'),
    path('calendar/<int:pk>/delete', views.CalendarDelete.as_view(), name='calendar_delete'),
    path('homework', views.homework, name='homework'),
    path('create_homework', views.create_homework, name='create_homework'),
    path('homework/<int:pk>/update', views.HomeworkUpdate.as_view(), name='homework_update'),
    path('homework/<int:pk>/delete', views.HomeworkDelete.as_view(), name='homework_delete'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('user_profile/<int:pk>/update', views.UserProfileUpdate.as_view(), name='user_profile_update'),
    path('user_profile/<int:pk>/update_speech', views.UserProfileUpdateSpeech.as_view(), name='user_profile_update_speech'),
    path('user_profile/<int:pk>/delete_speech', views.UserProfileDeleteSpeech.as_view(), name='user_profile_delete_speech'),
    path('create_user', views.CreateUser.as_view(), name='create_user'),
    path('archive', views.archive, name='archive'),
    path('statistics', views.statistics, name='statistics'),
]