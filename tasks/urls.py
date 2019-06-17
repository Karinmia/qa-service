from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.TaskUpdateView.as_view(), name='create_task'),
    path('delete/<uuid:pk>', views.TaskDeleteView.as_view(), name='delete_task'),
    path('done/<uuid:pk>', views.TaskDone.as_view(), name='done_task'),
    path('update/<uuid:pk>', views.TUpdateView.as_view(), name='update_task')
]
