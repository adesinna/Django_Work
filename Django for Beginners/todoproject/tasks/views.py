from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    tasks_list = Task.objects.all()
    tags_list = Tag.objects.all()
    context = {
        'tasks_list': tasks_list,
        'tags_list': tags_list
    }
    return render(request, 'tasks/tasks.html', context)

@login_required(login_url='accounts:login')
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            new_task = form.save()
            return redirect('accounts:dashboard')
    else:
        form = TaskForm()

    context = {
        'form': form
    }

    return render(request, 'tasks/add_task.html', context)

@login_required(login_url='accounts:login')
def add_tag(request):
    if request.method == 'POST':
        form = TagForm(data=request.POST)
        form.instance.user = request.user
        if form.is_valid():
            new_tag = form.save()
            return redirect('accounts:dashboard')
    else:
        form = TagForm()

    context = {
        'form': form
    }

    return render(request, 'tasks/add_tag.html', context)