from django import forms
from kanban.models import Task, Diary

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ('title', 'deadline', 'status')

class DiaryForm(forms.ModelForm):
  class Meta:
    model = Diary
    fields = ('title', 'text')