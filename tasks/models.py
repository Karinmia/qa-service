import uuid

# from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=500, blank=True)
    jira_ticket = models.CharField(max_length=100, blank=True)
    confluence_page = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     """ On save, update timestamps """
    #     if not self.id:
    #         self.created_at = timezone.now()
    #     self.updated_at = timezone.now()
    #     return super(Task, self).save(*args, **kwargs)
