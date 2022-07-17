from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.


def task(request):
    tasks_list = Task.objects.all()
    context = {
        'tasks_list': tasks_list
    }

    return render(request, 'finalapp/tasks.html', context)


def create_task(request):
    context = {}
    if request.method == 'POST':
        content = request.POST['content']  # get content data
        deadline = request.POST['deadline']
        new_task = Task(content=content, deadline=deadline)
        new_task.save()
        return redirect('finalapp:tasks')  # the name in the url

    else:
        return render(request, 'finalapp/create_task.html', context)


def contact(request):
    context = {}
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']

        return redirect('finalapp:tasks')

    else:
        return render(request, 'finalapp/contact.html', context)


def django_contact(request):

    if request.method == 'POST':
        form = ContactForm(data=request.POST)  # this will get all the data
        if form.is_valid():
            return redirect('finalapp:tasks')

    else:
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'finalapp/django_contact.html', context)


def django_task(request):

    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save()
            return redirect('finalapp:tasks')

    else:  # if it's a get request which is what will happen first
        form = TaskForm()
        context = {
            'form': form
        }
        return render(request, 'finalapp/django_task.html', context)  # show the form



