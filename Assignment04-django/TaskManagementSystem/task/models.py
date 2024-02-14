from django.db import models
from category.models import Category
# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=30)
    taskDescription = models.TextField(max_length=300)
    isComplete = models.BooleanField(default=False)
    taskAssignDate = models.DateField()
    taskCategory = models.ManyToManyField(Category)

    def __str__(self):
        return self.taskTitle