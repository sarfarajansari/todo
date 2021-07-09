from django.urls import path

from . import views

urlpatterns = [
    path('room/<str:room_name>/<str:player>/', views.room, name='room'),
    path('room/<str:room_name>/', views.room, name='room'),
    path("game/create/",views.createGame,name='create'),
    path("game/join/",views.joinGame,name='join'),
]