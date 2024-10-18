from django.db import models

# Create your models here.
class TodoItem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)

