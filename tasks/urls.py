from django.urls import path
from . import views


app_name = "tasks"


urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_task, name="task-create"),
    path("list/", views.list_task, name="task-list"),
    path("search/", views.search_task, name="task-search"),
    path("tag/<slug:tag_slug>", views.list_task, name="task-list-by-tag"),
    path("<int:pk>/edit", views.edit_task, name="task-edit"),
    path("<int:pk>/delete", views.delete_task, name="task-delete"),
    path("<int:pk>/detail", views.task_detail, name="task-detail"),
]
