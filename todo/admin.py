from django.contrib import admin
from .models import TaskUser,Task
# Register your models here.

admin.site.register(Task)
admin.site.register(TaskUser)
