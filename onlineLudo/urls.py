from django.urls import path

from . import views

urlpatterns = [
    path('room/<str:room_name>/<str:player>/', views.room, name='room'),
    path('room/<str:room_name>/', views.room, name='room'),
    path("create/",views.create,name='create'),
    path("join/",views.join,name='join'),
    path("sendmessage/",views.sendMessage,name='send'),
    path("connect/<str:gtoken>/<str:ptoken>/",views.Connect,name='connect'),
    path("disconnect/<str:gtoken>/<str:ptoken>/",views.Disconnect,name='disconnect'),
    path("update/message/<str:gtoken>/<str:ptoken>/",views.updateMessage,name="message"),
]