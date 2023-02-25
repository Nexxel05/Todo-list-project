from django.contrib import admin

from app.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Tag)