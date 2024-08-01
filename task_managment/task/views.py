from .models import Task
from .forms import TaskForm
from django.shortcuts import render, redirect


def index(request):
    task_list = Task.objects.order_by('-start_date')
    context = {
        'task_list': task_list,
    }
    return render(request, 'task/index.html', context)


def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    title = task.text[0:30]
    context = {
        'task': task,
        'title': title,
        'task_id': task_id
    }
    return render(request, 'task/task_detail.html', context)


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            return redirect('task:index')
    else:
        form = TaskForm()
    return render(request, 'task/create_task.html', {'form': form})


def update(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task:index')


def update2(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = task.completed
    task.save()
    return redirect('task:index')


def delete(task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return render(redirect('task/index.html'), task, task_id)
