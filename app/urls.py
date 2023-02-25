from django.urls import path

from app.views import (
    index,
    TagListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/create", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("tags", TagListView.as_view(), name="tag-list"),
]

app_name = "app"
