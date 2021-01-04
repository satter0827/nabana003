from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from kanban.models import Task
from kanban.forms import TaskForm

# Create your views here.
class KanbanView(LoginRequiredMixin, TemplateView):
  template_name = 'kanban/home.html'

class TaskListView(LoginRequiredMixin, ListView):
  model = Task
  template_name = 'kanban/task_index.html'
  paginate_by = 20

class TaskCreateView(LoginRequiredMixin, CreateView):
  model = Task
  form_class = TaskForm
  template_name = "kanban/task_create.html"
  success_url = "/kanban/home"

class TaskUpdateView(LoginRequiredMixin, UpdateView):
  model = Task
  form_class = TaskForm
  template_name = "kanban/task_update.html"
  success_url = "/kanban/task_index"

class TaskDeleteView(LoginRequiredMixin, DeleteView):
  model = Task
  form_class = TaskForm
  success_url = "/kanban/task_index"

  def delete(self, request, *args, **kwargs):
    result = super().delete(request, *args, **kwargs)
    messages.success(self.request, "タスクを削除しました")
    return result