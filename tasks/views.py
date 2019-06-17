from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from bootstrap_modal_forms.generic import BSModalDeleteView, BSModalUpdateView

from .models import Task
from . import forms


def task_list(request):
    tasks = Task.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


class TaskUpdateView(CreateView):
    model = Task
    fields = ('title', 'description')
    template_name = 'tasks/update_task.html'
    success_url = reverse_lazy(task_list)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        print("DEBUG: success")
        return redirect(task_list)


class TaskDeleteView(BSModalDeleteView):
    model = Task
    template_name = 'tasks/delete_task.html'
    success_message = 'task_list'
    success_url = reverse_lazy(task_list)


class TUpdateView(BSModalUpdateView):
    model = Task
    form_class = forms.TaskForm
    template_name = 'tasks/update_task.html'
    success_url = reverse_lazy(task_list)


class TaskDone(BSModalUpdateView):
    model = Task
    form_class = forms.TaskCheck
    template_name = 'tasks/done_task.html'
    success_url = reverse_lazy(task_list)

    def form_valid(self, form):
        if form.instance.done == False:
            form.instance.done = True
        else:
            form.instance.done = False
        form.save()
        print("DEBUG: success")
        return redirect(task_list)
