from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Task
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm  # register
from django.contrib.auth import login

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True  # if user is authenticated they should not be allowed to be in the login page

    def get_success_url(self):  # use this function whenever you need success url in login
        return reverse_lazy('todo:task_list')


class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm  # django form
    success_url = reverse_lazy('todo:task_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:  # if user is authenticated log in the user!
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    # we need to prevent authenticated user from registering!

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo:task_list')  # this is the page it will return instead of signing up
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):  # LoginRequiredMixin is just like the decorator login require, and it must come first in the tuple
    model = Task
    context_object_name = 'tasks_list'  # instead of saying object_list in the template we can use this!

    def get_context_data(self,  **kwargs):  # this ensures that each user gets his own data
        context = super().get_context_data(**kwargs)
        context['tasks_list'] = context['tasks_list'].filter(user=self.request.user)  # filter by user task
        # add more data like count the uncompleted data
        context['count'] = context['tasks_list'].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''  # the search
        if search_input:
            context['tasks_list'] = context['tasks_list'].filter(title__startswith=search_input)
        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'  # that is each i in the list name is context
    # template_name = app/name.html in case you want your own name


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/add_task.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todo:task_list')  # this is like redirect

    def form_valid(self, form):  # to make sure the user is the one creating the form! without having to use the user field to choose
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/edit_task.html'
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('todo:task_list')  # this is like redirect


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'todo/delete_task.html'
    success_url = reverse_lazy('todo:task_list')
