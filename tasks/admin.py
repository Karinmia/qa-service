from django.contrib import admin
from .models import Task


admin.site.register(Task)
admin.site.site_header = "QA Helper"
admin.site.site_title = "QA Helper"
