from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'description', 'start_date', 'completed')
    list_editable = ('text', 'description')
    search_fields = ('text')
    list_filter = ('start_date')


admin.site.register(Task, TaskAdmin)
