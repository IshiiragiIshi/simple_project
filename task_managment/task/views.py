from .models import Task
from .forms import TaskForm
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    task_list = Task.objects.order_by('-start_date')
    context = {
        'task_list': task_list,
    }
    return render(request, 'task/index.html', task_list, context)


def task_detail(request):
    task = get_object_or_404(Task)
    title = task.text[0:30]
    context = {
        'task': task,
        'title': title,
    }
    return render(request, 'task/index.html', context)


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task/index.html')
    else:
        form = TaskForm()
    return render(request, 'task/create_task.html', {'from': form})
# Create your views here.
