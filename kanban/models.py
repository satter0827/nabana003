from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from datetime import datetime

import uuid as uuid_lib

# Create your models here.
class Task(models.Model):
  task_id = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)
  name = models.CharField(null=False, max_length=50)
  deadline = models.DateField()
  done = models.BooleanField(default=False)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return self.task_id