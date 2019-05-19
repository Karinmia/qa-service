import uuid

from django.db import models


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    jira_id = models.CharField(max_length=100, blank=True)
    confluence_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username
