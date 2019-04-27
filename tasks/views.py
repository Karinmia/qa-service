from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Task


def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})
