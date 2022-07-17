from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from .forms import CreateUserForm
from tasks.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # we check whether the user exist
        if user is not None:
            user_login(request, user)  # login the user if it is found
            return redirect('accounts:dashboard')
        else:  # if user is not found
            messages.error(request, 'Username or Password is incorrect')  # check accounts/login.html to see how it works!
    return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:login')

    else:
        form = CreateUserForm()

    context = {  # this context is for both forms, either on that goes through becomes the context
        'form': form
    }
    return render(request, 'accounts/register.html', context)


def logout(request):
    user_logout(request)  # log the user out
    return redirect('accounts:login')


@login_required(login_url='accounts:login')  # makesure they log in or redirect them to login
def dashboard(request):
    user = request.user
    tasks_list = user.task_set.all()
    tags_list = user.tag_set.all()
    context = {
        'tasks_list': tasks_list,
        'tags_list': tags_list,
    }
    return render(request, 'pages/dashboard.html', context)
