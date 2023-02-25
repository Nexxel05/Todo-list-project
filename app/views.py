from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from app.models import Task, Tag


def index(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "app/index.html", context)


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("app:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("app:index")


class TagListView(generic.ListView):
    model = Tag
