from time import sleep
from threading import Timer
from .models import LectureTime
from datetime import datetime,timedelta
import pytz

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)
        

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True
            if self.interval < 3595:
                minutes = 60 - datetime.now().minute
                seconds = 60 - datetime.now().second
                self.interval = minutes * 60 + seconds

    def stop(self):
        self._timer.cancel()
        self.is_running = False


def updateDB():
    today =datetime.now().weekday()
    lectures = LectureTime.objects.filter(dayId = today)
    for lecture in lectures:
        lectime = lecture.datetime + timedelta(minutes=lecture.lecture.duration)
        now = datetime.utcnow() + timedelta(hours=5,minutes=30)
        now = pytz.utc.localize(dt=now)
        if now.hour >= lectime.hour and now.minute>=lectime.minute and now.date()==lectime.date():
            lecture.datetime+= timedelta(hours=168)
            lecture.save()
            print("lecture updated for next week")


def run():
    print("starting...")
    rt = RepeatedTimer(1
    , updateDB) # it auto-starts, no need of rt.start()
    try:
        sleep(3153600)
        sleep(3153600)
        sleep(3153600)
        sleep(3153600)
        sleep(3153600)
        sleep(3153600)
        sleep(3153600)
        sleep(3153600)
        sleep(3153600)
        sleep(3153600)
        sleep(3153600)
        sleep(3153600)
        sleep(3153600)
        sleep(3153600)
        sleep(3153600) # your long-running job goes here...
    finally:
        rt.stop() 

# t = Timer(1,run)
# t.start()

