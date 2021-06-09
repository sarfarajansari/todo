from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TaskUser(models.Model):
    user=models.OneToOneField(User,max_length=64,blank=True,on_delete=models.CASCADE,null=True)
    key = models.CharField(max_length=40)

    def __str__(self):
        return self.key

class Task(models.Model):
    task=models.CharField(max_length=500)
    done=models.BooleanField(default=False)
    start_date=models.DateField(auto_now_add=True)
    complete_date=models.DateField(blank=True,null=True)
    user=models.ForeignKey(TaskUser,on_delete=models.CASCADE,related_name="tasks")

    def __str__(self):
        return self.task