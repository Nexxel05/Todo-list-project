from django.shortcuts import render
from django.views import generic

from app.models import Task, Tag


def index(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "app/index.html", context)


class TagListView(generic.ListView):
    model = Tag
