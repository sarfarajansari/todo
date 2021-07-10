from django.urls import path
from .import views

urlpatterns =[
    path("initialize/",views.newGame,name="initializegame"),
    path("getgame/<str:token>/",views.getGame,name="getGame"),
    path("play/<str:token>/",views.Play,name="play"),
    path("nextplayer/<str:token>/",views.nextplayer,name="nextplayer"),
    path("message/",views.sendMessage,name="sendMessage"),
    path("getmsgs/<str:token>/",views.getMessage,name="getMessage"),
    path("test/",views.test,name="test"),
]