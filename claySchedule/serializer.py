from datetime import datetime,timedelta
from rest_framework import serializers


class responseSerializer(serializers.Serializer):
    subject = serializers.CharField()
    teacher = serializers.CharField()
    duration = serializers.IntegerField()
    link = serializers.CharField()
    day = serializers.CharField()
    dayId = serializers.IntegerField()
    starttime = serializers.DateTimeField()
    endtime = serializers.DateTimeField()
    secondLeft = serializers.IntegerField()
    hourLeft = serializers.IntegerField()
    minuteLeft = serializers.IntegerField()
    status = serializers.IntegerField()



class responsedata:
    def __init__(self,lecture):
        self.subject = lecture.subject
        self.teacher = lecture.teacher
        self.duration = lecture.duration
        self.link = lecture.link
        self.day = lecture.day.get(dayId=lecture.get_next_lecture).day
        self.dayId = lecture.get_next_lecture
        self.starttime = lecture.lectime
        self.endtime = self.starttime + timedelta(minutes=self.duration)
        self.secondLeft = self.getSecond()
        self.hourLeft = self.secondLeft/3600
        self.minuteLeft = self.getMinute()
        self.status = self.get_status()
        
    def get_status(self):
        if self.getNow()< self.starttime:
            return 0
        elif self.getNow()>=self.starttime and self.getNow() <self.endtime:
            return 1
        else:
            return 2
    def getNow(self):
        now = datetime.utcnow() + timedelta(hours=5,minutes=30) 
        return now

    def getSecond(self):
        delta =self.starttime- (self.getNow() )
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