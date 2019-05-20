from .models import Task
from bootstrap_modal_forms.forms import BSModalForm


class TaskForm(BSModalForm):
    class Meta:
        model = Task
        fields = ['title',
                  'author',
                  'description'
                  ]
