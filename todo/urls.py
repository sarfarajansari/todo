from django.urls import path
from .import views

urlpatterns =[
    path("get/<int:done>/<str:token>/",views.getTasks),
    path("complete/",views.completeTask),
    path("delete/",views.delTask),
    path("post/",views.postTask),
]