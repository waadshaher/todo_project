from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Task

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')