from django.contrib import admin
from django.utils import timezone

from .models import *

# Register your models here.


def mark_complete(model_admin, request, queryset):
    queryset.update(
        status=TaskStatus.COMPLETED,
        completed_at=timezone.now()
    )


mark_complete.short_description = 'complete'  # short descriptions


def mark_pending(model_admin, request, queryset):
    queryset.update(
        status=TaskStatus.PENDING,
        completed_at=timezone.now()
    )


def mark_dropped(model_admin, request, queryset):
    queryset.update(
        status=TaskStatus.DROPPED,
        completed_at=timezone.now()
    )


class TaskAdmin(admin.ModelAdmin):
    fields = [
        'content',  # first row
        ('deadline', 'tag')  # second row and put them side by side
    ]

    list_display = ['content', 'status', 'deadline']  # this is what you see before clicking to edit it
    list_editable = ['status']  # the editable things at the interface
    actions = [mark_complete, mark_dropped, mark_pending]  # actions you want to show
    list_filter = ['status', 'deadline']  # shows the filter!
    search_fields = ['content', 'tag__name']  # allows you to search
    ordering = ['-deadline']

    def get_ordering(self, request):
        if request.user.is_superuser:  # super user privilege
            return ['status']
        else:
            return ['-deadline']

admin.site.register(Task, TaskAdmin)  # the fields in TaskAdmin that what will show!
admin.site.register(Tag)

