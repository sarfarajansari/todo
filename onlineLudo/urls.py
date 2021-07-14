from django.urls import path

from . import views

urlpatterns = [
    path("create/",views.create,name='create'),
    path("join/",views.join,name='join'),
    path("sendmessage/",views.sendMessage,name='send'),
    path("connect/<str:gtoken>/<str:ptoken>/",views.Connect,name='connect'),
    path("disconnect/<str:gtoken>/<str:ptoken>/",views.Disconnect,name='disconnect'),
    path("update/message/<str:gtoken>/<str:ptoken>/",views.updateMessage,name="message"),
    path("update/game/<str:gtoken>/<str:ptoken>/",views.updateGame,name="message"),
    path("play/<str:gtoken>/<str:ptoken>/",views.play,name="play"),
]