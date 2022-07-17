from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', TemplateView.as_view(template_name='tasks/index.html'), name='index'),
    path('today/', TemplateView.as_view(template_name='tasks/today.html'), name='today'),
    path('page1/', views.page, name='page')

]
