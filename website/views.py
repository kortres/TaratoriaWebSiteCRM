from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from crm.forms import Registration


def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


def location(request):
    return render(request, 'website/location.html')


def log(request):
    redirect('accounts/login')


class SignUp(CreateView):
    form_class = Registration
    success_url = reverse_lazy("login")
    template_name = "crm/signup.html"