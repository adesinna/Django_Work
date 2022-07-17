from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView  # log out is done only for urls not in views

app_name = 'todo'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='todo:login'), name='logout'), # and go and put LOGIN_URL = 'todo:login' in settings
    path('signup/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(), name='task_list'),  # the template name is task_list and object_list as list name comes as default in the class based view and list do not need pk since it brings out the whole list!
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('create_task/', TaskCreate.as_view(), name='task_create'),  # create do not need pk since it is auto for it
    path('update_task/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('delete_task/<int:pk>/', TaskDelete.as_view(), name='task_delete'),


]
