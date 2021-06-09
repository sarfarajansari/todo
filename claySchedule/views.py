from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime,timedelta
from .models import Lecture
from .serializer import responsedata
import pytz
from authApi.models import ClayStudent
# Create your views here.

def student(request):
    if request.user.is_authenticated:
        try: 
            student = ClayStudent.objects.get(student=request.user)
            return True
        except:
            pass
    return True
@api_view(["GET"])
def index(request):
    if student(request):
        lectures = Lecture.objects.all()
        Data=[]
        for lec in lectures:
            Data.append(responsedata(lec).data)
        return Response(Data)
    return Response([])
