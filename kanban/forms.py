from django import forms
from kanban.models import Task

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ('name', 'deadline', 'done')