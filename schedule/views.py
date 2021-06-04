from .import task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime,timedelta
from .serializer import responsedata
from .models import LectureTime,ClayStudent
import pytz


def student(request):
    if request.user.is_authenticated:
        try: 
            student = ClayStudent.objects.get(student=request.user)
            return True
        except:
            pass
    return False
@api_view(["GET"])
def index(request):
    if student(request):
        today =datetime.now().weekday()
        todayLectures = LectureTime.objects.filter(dayId = today)
        tomLectures = LectureTime.objects.filter(dayId = today +1)
        lectures = list(todayLectures) + list(tomLectures)
        now = datetime.utcnow() + timedelta(hours=5,minutes=30)
        now = pytz.utc.localize(dt=now)
        Data = []
        for lec in lectures:
            lectime = lec.datetime + timedelta(minutes=lec.lecture.duration)
            if lec.dayId == today:
                if now<lectime and now.hour >= lectime.hour and now.minute>=lectime.minute:
                    pass
                else:
                    Data.append(responsedata(lec).data)
            else:
                Data.append(responsedata(lec).data)
        return Response(Data)
    return Response([])