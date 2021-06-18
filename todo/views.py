from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime,timedelta
from .models import TaskUser,Task
from .serializer import TaskSerializer
from store.views import get_random_string


@api_view(["GET"])
def getTasks(request,done,token):
    if token =="create":
        key = get_random_string(20)
        TaskUser.objects.create(key=key)
        return Response({"status":0,"tasks":[],"token":key})
    try:
        user = TaskUser.objects.get(key=token)
        if done==0:
            tasks = user.tasks.filter(done=False)
        elif done==1:
            tasks = user.tasks.filter(done=True)
        else:
            return Response({"status":1,"message":"Invalid filter"})
        data = TaskSerializer(tasks,many=True).data
        return Response({"tasks":data,"status":0})
    except:
        return Response({"status":1,"message":"User not found"})

def taskofUser(user):
    tasks = user.tasks.filter(done=False)
    data = TaskSerializer(tasks,many=True).data
    return data

@api_view(["POST"])
def postTask(request):
    data = request.data
    if "token" in data and "task" in data:
        try:
            user = TaskUser.objects.get(key=data["token"])
        except:
            return Response({"status":1,"message":"User not found"})
        Task.objects.create(task=data["task"],done=False,user=user)
        return Response({"status":0,"message":"Task added","tasks":taskofUser(user)})
    return Response({"status":1,"message":"Invalid task"})


@api_view(["POST"])
def completeTask(request):
    data = request.data
    if "token" in data and "id" in data:
        try:
            user = TaskUser.objects.get(key=data["token"])
        except:
            return Response({"status":1,"message":"User not found"})
        task = Task.objects.get(user=user,pk=data["id"])
        task.done = True
        task.complete_date = datetime.utcnow() + timedelta(hours=5,minutes=30)
        task.save()
        return Response({"status":0,"message":"Task Completed","tasks":taskofUser(user)})
    return Response({"status":1,"message":"Invalid task"})

@api_view(["POST"])
def delTask(request):
    data = request.data
    if "token" in data and "id" in data:
        try:
            user = TaskUser.objects.get(key=data["token"])
        except:
            return Response({"status":1,"message":"User not found"})
        task = Task.objects.get(user=user,pk=data["id"])
        task.delete()
        return Response({"status":0,"message":"Task Deleted","tasks":taskofUser(user)})
    return Response({"status":1,"message":"Invalid task"})