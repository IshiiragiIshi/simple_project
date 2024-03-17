from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('text', 'description')
        labels = {'text': 'Заголовок', 'description': 'Описание'}
