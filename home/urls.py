from django.urls import path
from . import views

urlpatterns =[

    path('projects/',views.projectsApi,name="projectsApi"),
    path('project/<int:pk>/',views.projectApi,name="projectApi"),
    path('message/',views.messageApi,name="messageApi"),

]