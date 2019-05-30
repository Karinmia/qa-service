from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from bootstrap_modal_forms.generic import (BSModalCreateView, BSModalDeleteView)

from .forms import TaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# class TaskCreateView(BSModalCreateView):
#     template_name = 'tasks/create_task.html'
#     form_class = TaskForm
#     success_url = reverse_lazy(task_list)
#

class TaskUpdateView(CreateView):
    model = Task
    fields = ('title', 'description')
    template_name = 'tasks/update_task.html'
    success_url = reverse_lazy(task_list)


class TaskDeleteView(BSModalDeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_message = 'Success: task was deleted'
    success_url = reverse_lazy(task_list)
