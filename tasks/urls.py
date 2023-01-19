from django.urls import path
from . import views


app_name = "tasks"


urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_task, name="task-create"),
    path("list/", views.list_task, name="task-list"),
    path("<int:pk>/edit", views.edit_task, name="task-edit"),
    path("<int:pk>/delete", views.delete_task, name="task-delete"),
    path("<int:pk>/mark-completed", views.mark_completed, name="task-completed"),
]
