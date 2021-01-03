from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

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

