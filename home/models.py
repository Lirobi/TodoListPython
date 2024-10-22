from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoItem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    user = models.CharField(models.ForeignKey(User, on_delete=models.CASCADE))

