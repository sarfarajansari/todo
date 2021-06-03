from rest_framework import serializers
from .models import Lecture,LectureTime
from datetime import datetime, timedelta
import pytz



class responseSerializer(serializers.Serializer):
    subject = serializers.CharField()
    teacher = serializers.CharField()
    duration = serializers.IntegerField()
    link = serializers.CharField()
    day = serializers.CharField()
    dayId = serializers.IntegerField()
    starttime = serializers.DateTimeField()
    endtime = serializers.DateTimeField()
    starthour = serializers.IntegerField()
    startminute = serializers.IntegerField()
    endhour = serializers.IntegerField()
    endminute = serializers.IntegerField()
    currentTime = serializers.DateTimeField()
    secondLeft = serializers.IntegerField()
    hourLeft = serializers.IntegerField()
    minuteLeft = serializers.IntegerField()


class responsedata:
    def __init__(self,obj):
        self.subject = obj.lecture.subject
        self.teacher = obj.lecture.teacher
        self.duration = obj.lecture.duration
        self.link = obj.lecture.link
        self.day = obj.day
        self.dayId = obj.dayId
        self.starttime = obj.datetime
        self.endtime = obj.datetime + timedelta(minutes=self.duration)
        self.starthour = self.starttime.hour
        self.startminute = self.starttime.minute
        self.endhour = self.endtime.hour
        self.endminute = self.endtime.minute
        self.currentTime = self.getNow()
        self.secondLeft = self.getSecond()
        self.hourLeft = self.secondLeft/3600
        self.minuteLeft = self.getMinute()

    def getNow(self):
        now = datetime.utcnow()
        now = pytz.utc.localize(dt=now)
        return now

    def getSecond(self):
        delta =self.starttime- (self.currentTime + timedelta(hours=5,minutes=30) )
        seconds = delta.total_seconds()
        return seconds
    
    def getMinute(self):
        seconds = self.secondLeft
        hours = self.hourLeft
        delta = int(seconds) - (int(hours) *3600)
        return delta/60



    @property
    def data(self):
        return responseSerializer(self).data