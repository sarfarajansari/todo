from django.db import models
from datetime import datetime,timedelta
from django.contrib.auth.models import User

class Day(models.Model):
    day = models.CharField(max_length=30)
    dayId = models.IntegerField()

    def __str__(self):
        return self.day

class Time(models.Model):
    hour = models.IntegerField()
    minute = models.IntegerField()

    def __str__(self):
        return str(self.hour) +" : " + str(self.minute)
# class ClayStudents(models.Model):
#     rollNo = models.IntegerField()
#     student = models.ForeignKey(User,on_delete=models.CASCADE,related_name="student")

#     def __str__(self):
#         return self.rollNo

class Lecture(models.Model):
    subject = models.CharField(max_length=30)
    teacher = models.CharField(max_length=40,default="")
    duration = models.IntegerField()
    link = models.CharField(max_length=150)
    day = models.ManyToManyField(Day,related_name="lectures",blank=True)
    time = models.ForeignKey(Time, related_name="lectures",on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return f"{self.subject} with {self.teacher} "  

    @property
    def lectime(self):
        date = datetime.utcnow() + timedelta(hours=5,minutes=30)
        today = date.weekday()
        date = datetime.combine(date.date(),datetime.min.time())
        nextLecture = self.nextLec(today,self.get_days()[0],self.get_days()[1],self.get_days()[2])
        date = self.get_date(date,nextLecture) + timedelta(hours=self.time.hour,minutes=self.time.minute)
        return date
    
    @property
    def get_next_lecture(self):
        date = datetime.utcnow() + timedelta(hours=5,minutes=30)
        today = date.weekday()
        date = datetime.combine(date.date(),datetime.min.time())
        nextLecture = self.nextLec(today,self.get_days()[0],self.get_days()[1],self.get_days()[2])
        return nextLecture
    def get_date(self,date,lec):
        if date.weekday()==lec:
            return date
        return self.get_date(date+timedelta(hours=24),lec)
    def get_days(self):
        days=[]
        for day in self.day.all():
            days.append(day.dayId)
        return days
    def nextLec(self,now,a,b,c):
        stepA=self.step(now,a,0)
        stepB=self.step(now,b,0)
        stepC=self.step(now,c,0)
        if stepA<stepB:
            if stepA<stepC:
                return a
            else:
                return c
        else:
            if stepB<stepC:
                return b
            else:
                return c
    def next(self,now):
        if now<5:
            return now+1
        else:
            return 0

    def step(self,now,lec,s):
        if now==lec:
            return s
        return self.step(self.next(now),lec,s+1)
    