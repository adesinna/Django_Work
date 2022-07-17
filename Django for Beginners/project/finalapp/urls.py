from django.urls import path

from . import views

app_name = 'finalapp'  # so you can go there

urlpatterns = [
    path('tasks/', views.task, name='tasks'),
    path('add_task', views.create_task, name='add_task'),
    path('contact_page', views.contact, name='contact'),
    path('django_contact', views.django_contact, name='django_contact'),
    path('django_task', views.django_task, name='django_task')
]
