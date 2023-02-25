from django.urls import path

from app.views import (
    index,
    TagListView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    toggle_complete_status,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/toggle_complete_status/", toggle_complete_status, name="task-toggle_complete_status"),

    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

]

app_name = "app"
