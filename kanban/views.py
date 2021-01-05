from django.shortcuts import render

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from kanban.models import Task, Diary
from kanban.forms import TaskForm, DiaryForm

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
  success_url = "/kanban/task_index"

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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

class DiaryListView(LoginRequiredMixin, ListView):
  model = Diary
  template_name = 'kanban/diary_index.html'
  paginate_by = 20

class DiaryCreateView(LoginRequiredMixin, CreateView):
  model = Diary
  form_class = DiaryForm
  template_name = "kanban/diary_create.html"
  success_url = "/kanban/diary_index"

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DiaryUpdateView(LoginRequiredMixin, UpdateView):
  model = Diary
  form_class = DiaryForm
  template_name = "kanban/diary_update.html"
  success_url = "/kanban/diary_index"

class DiaryDeleteView(LoginRequiredMixin, DeleteView):
  model = Diary
  form_class = DiaryForm
  success_url = "/kanban/diary_index"

  def delete(self, request, *args, **kwargs):
    result = super().delete(request, *args, **kwargs)
    messages.success(self.request, "日記を削除しました")
    return result