from django.db import models
from django.utils import timezone

# Create your models here.
class ToDoList(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class ToDoItem(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    due_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"Title : {self.title} | Description : {self.description} \
            | Due Date: {self.due_date}" 
