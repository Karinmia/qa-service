from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.urls import reverse_lazy
from .forms import TaskForm
from .models import Task
from bootstrap_modal_forms.generic import BSModalCreateView

from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})


class TaskCreateView(BSModalCreateView):
    template_name = 'tasks/create_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
