from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.task_create, name='create'),
    path('detail/<int:task_id>', views.task_detail, name='detail'),
    path('detail/<int:task_id>/update', views.update, name='update'),
    path('delete/<int:task_id>', views.delete, name='delete1')
]
