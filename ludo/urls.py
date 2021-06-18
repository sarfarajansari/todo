from django.urls import path
from .import views

urlpatterns =[
    path("game/<str:action>/",views.newGame,name="game"),
    path("play/<str:token>/",views.Play,name="play"),
    path("test/",views.test,name="test"),
]