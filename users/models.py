import uuid
from django.db import models


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True)
    jira_login = models.CharField(max_length=100, blank=True)
    jira_password = models.CharField(max_length=50, blank=True)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

