from django.urls import path
from .views import TaskCreate, TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task-create/',TaskCreate.as_view(), name = 'task-create'),
]