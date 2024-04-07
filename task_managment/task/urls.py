from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.task_create, name='create'),
    path('detail/<int:id>', views.task_detail, name='detail')
]
