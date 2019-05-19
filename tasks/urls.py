from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.TaskCreateView.as_view(), name='create_task')
    # path('task/<uuid:pk>/', views.task_details, name='task_details'),
    # path('task/new', views.task_edit, name='task_edit'),
    # path('task/<uuid:pk>/edit/', views.task_edit, name='task_edit'),
    # path('task/<uuid:pk>/delete', views.task_delete, name='task_delete')
]
