from django.urls import path
from .views import TaskCreate, TaskList, TaskUpdate, DeleteView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task-create/',TaskCreate.as_view(), name = 'task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]