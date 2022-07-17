from django.urls import path
from . import views

app_name = 'win'

urlpatterns = [
    path('', views.index, name='index'),
    path('players/', views.players, name='player')
]
