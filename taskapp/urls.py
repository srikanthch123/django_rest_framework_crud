from django.urls import path
from . import views

print("ssssssssssssssssss")

urlpatterns = [
    path('task-list', views.task_list, name='task-list'),
    path('create-task',views.create_task, name='create-task'),
    path('retrieve-task/<int:pk>', views.retrieve_task, name='task-retrieve'),
    path('update-task/<int:pk>', views.update_task, name='task-update'),
    path('delete-task/<int:pk>',views.delete_task, name='task-delete'),
]
