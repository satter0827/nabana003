from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid as uuid_lib

# Create your models here.
class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'CustomUser'

    user_id = models.UUIDField(default=uuid_lib.uuid4, primary_key=True, editable=False)
    