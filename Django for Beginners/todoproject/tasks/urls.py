from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='tasks'),
    path('add_task', views.add_task, name='add_task'),
    path('add_tag', views.add_tag, name='add_tag'),
]
