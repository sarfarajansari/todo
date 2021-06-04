from django.contrib import admin
from .models import Lecture,LectureTime,ClayStudent
# Register your models here.

admin.site.register(Lecture)
admin.site.register(LectureTime)
admin.site.register(ClayStudent)