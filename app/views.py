from django.shortcuts import render

from app.models import Task


def index(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "app/index.html", context)
