from . import views
from django.urls import path

urlpatterns = [
        
    path("", views.tasklist, name="tasklist"),
    path("create/", views.task_create, name="task_create"),  
    path("delete/<int:pk>/", views.task_delete, name="task_delete"),
    path("update/<int:pk>/", views.task_update, name="task_update"),

]