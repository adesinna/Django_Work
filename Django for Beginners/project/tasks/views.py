from datetime import datetime

from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse('This is task view')

# function based view with context


def page(request):
    context = {
        'name': 'Adesina',
        'days_list': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        'datetime': str(datetime.now())
    }
    return render(request, 'tasks/page1.html', context)
