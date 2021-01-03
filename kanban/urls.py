from django.contrib import admin
from django.urls import path
from kanban import views

app_name = 'kanban'
urlpatterns = [
  path('home/', views.KanbanView.as_view(), name='home'),
  path('task_index/', views.TaskListView.as_view(), name='task_index'),
  path('task_create/', views.TaskCreateView.as_view(), name='task_create'),
]