from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('location', views.location, name='location'),
    path('accounts/login', views.log),
    path("signup/", views.SignUp.as_view(), name="signup")
]