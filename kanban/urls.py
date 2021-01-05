from django.contrib import admin
from django.urls import path
from kanban import views

app_name = 'kanban'
urlpatterns = [
  path('home/', views.KanbanView.as_view(), name='home'),

  path('task_index/', views.TaskListView.as_view(), name='task_index'),
  path('task_create/', views.TaskCreateView.as_view(), name='task_create'),
  path('task_update/<uuid:pk>', views.TaskUpdateView.as_view(), name='task_update'),
  path('task_delete/<uuid:pk>', views.TaskDeleteView.as_view(), name='task_delete'),

  path('diary_index/', views.DiaryListView.as_view(), name='diary_index'),
  path('diary_create/', views.DiaryCreateView.as_view(), name='diary_create'),
  path('diary_update/<uuid:pk>', views.DiaryUpdateView.as_view(), name='diary_update'),
  path('diary_delete/<uuid:pk>', views.DiaryDeleteView.as_view(), name='diary_delete'),
]