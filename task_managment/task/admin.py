from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'start_date', 'completed')
    list_editable = ('text',)
    search_fields = ('title',)
    list_filter = ('start_date',)


admin.site.register(Task, TaskAdmin)
